import re
import time
from os import environ
from datetime import datetime
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from .gitinfo import GitInfo

class GitShowHistoryLogPlugin(BasePlugin):
    config_scheme = (
        ('max_number_of_commits', config_options.Type(int, default=5)),
    )

    def __init__(self):
        self.enabled = True
        self.from_git = GitInfo()

    def on_page_markdown(self, markdown, page, config, files):
        if not self.enabled:
            return markdown
        
        pos = re.search(r"\{\{(\s)*git_show_history_log(\s)*\}\}", markdown)
            
        list_of_git_commits = self.from_git.get_commits_for_file(page.file.abs_src_path, self.config['max_number_of_commits'])
        
        table_header = "| Version | Author | When | Message |\n" \
                       "|---------|--------|------|---------|\n"

        pos = markdown.find("{{ git_show_history_log }}")

        pos += len(table_header)

        markdown = re.sub(r"\{\{(\s)*git_show_history_log(\s)*\}\}",
                      table_header,
                      markdown,
                      flags=re.IGNORECASE)
        
        
        for commit in list_of_git_commits:
            author = str(commit.author)
            date = time.strftime('%Y-%m-%d, %H:%M:%S', time.gmtime(commit.committed_date))
            msg = commit.message.partition('\n')[0]
            tag = str(self.from_git.get_tag_for_commit(commit))
            
            newstr = "| " + tag + " | " + author + " | " + date + " | " + msg + " |\n"
            
            new_markdown = markdown[:pos] + newstr + markdown[pos:]
            
            markdown = new_markdown 
            
            pos += len(newstr)

        return markdown
