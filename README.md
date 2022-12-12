# mkdocs-git-show-history-log-plugin

MkDocs plugin that displays the history log table for a specified markdown file, 
based on last N number of git commits as follows:

| Version | Author    | When                 | Message      |
|---------|-----------|----------------------|--------------|
| 0.1     | Your Name | 2020-10-18, 07:05:08 | Your Message |


## Setup
Install the plugin using pip:

`pip install mkdocs-git-show-history-log-plugin`

Activate the plugin in `mkdocs.yml`:
```yaml
plugins:
  - search
  - git-show-history-log
```

More information about plugins in the [MkDocs documentation](mkdocs-plugins).

## Usage

### Markdown - `{{ git_show_history_log }}`:

#### Example
```md
**Changelog:**

{{ git_show_history_log }}
```

## Options

### `max_number_of_commits`

Setting this option will specify maximum number of commits(rows) per history log for the file. Default is set to 5.

