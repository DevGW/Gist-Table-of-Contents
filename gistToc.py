#!/usr/bin/python3
import requests
import re
import sys

class GistToc():
    def __init__(self, config):
        self.username = config['username']
        self.api_url = f"https://api.github.com/users/{self.username}/gists?per_page=50&"
        self.params = {'scope': 'gist'}
        self.toc_file = config['toc_file']
        self.tags = []
        self.gists = []
        self.categorized_dict = {}
        self.headers = {
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def get_gists(self):
        print(f"Generating TOC for {self.username}'s gists")
        page = 1
        gists = None
        while gists or page == 1:
            print(f"Getting gists page: {page}")
            res = requests.get(self.api_url + f"page={page}")
            gists = res.json()
            self.gists += gists
            ### get correct username casing
            if gists:
                self.username = gists[0]['owner']['login']
            # print(self.username)
            page += 1
        return self.gists

    def buildTagList(self):
        self.get_gists()
        for g in self.gists:
            self.tags = self.tags + re.findall(r'\#\w+', g['description'])

        ### remove dupes
        self.tags = [*set(self.tags)]
        self.tags.sort(key=str.casefold)

    def categorize(self):
        for g in self.gists:
            ### build TOC item
            item = {
                'description': g['description'],
                'url': g['html_url'],
                'tags': None
            }

            tags_found = [ele for ele in self.tags if(ele in g['description'])]
            if not tags_found:
                tags_found.append('#Uncategorized')
            item['tags'] = tags_found
            for tf in tags_found:
                if tf == '#Uncategorized' and tf not in self.tags:
                    self.tags.append(tf)
                if self.categorized_dict.get(tf) == None:
                    self.categorized_dict[tf] = []

                self.categorized_dict[tf].append(item)

    def buildToc(self):
        toc = f"""
# {self.username}'s Gists
## Table of Contents
"""
        toc += "### Categories: "
        i = 0
        for t in self.tags:
            toc += f"[{t}]({t}-{len(self.categorized_dict[t])}){ '' if i == len(self.tags) -1 else ' | ' }"
            i += 1
        for tag in self.tags:
            toc += f"\n### {tag.replace('#', '')} (*{len(self.categorized_dict[tag])}*)\n"
            for entry in self.categorized_dict[tag]:
                # print(entry)
                toc += f"""
* #### [{entry['description']}]({entry['url']})
> #### *Tags: {', '.join(entry['tags'])}*
                """

        ### write to file
        fd = open(self.toc_file, 'w')
        fd.write(toc)
        fd.close()
        print(f"Generated TOC with {len(self.tags)} categories and {len(self.gists)} entries")
        print(f"Your Table of Contents can be found here: ./{self.toc_file}")

def procArgs(args):
    if not len(args) == 2:
        print(f"Usage: {args[0]} GITHUB_USERNAME")
        exit()

    config = {
        'username': args[1],
        'toc_file': 'table_of_contents.md'
    }
    gisttoc = GistToc(config)
    gisttoc.buildTagList()
    gisttoc.categorize()
    gisttoc.buildToc()

if __name__ == '__main__':
    procArgs(sys.argv)
