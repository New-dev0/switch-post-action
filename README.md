# New-dev0/switch-post-action@v1

This action allows you to send messages to a Switch community, group, or user using the Switch API.

## Inputs

| Name | Description | Required |
|------|-------------|----------|
| `token` | Switch's bot token | Yes |
| `message` | Message text to send | No |
| `document` | Path to file to send as document | No |
| `description` | Description for the document | No |
| `thumb` | Path to thumbnail image | No |
| `channel_id` | Switch channel ID (requires `community_id`) | No |
| `group_id` | Switch group ID (requires `community_id`) | No |
| `community_id` | Switch community ID | No |
| `user_id` | Switch user ID for direct messages | No |
| `button_text` | Text to display on the button | No |
| `button_url` | URL to open when the button is clicked | No |

## Usage

### Basic Example: Send a text message to a user

```yaml
- name: Send a text message to a user
  uses: New-dev0/switch-post-action@v1
  with:
    token: ${{ secrets.SWITCH_BOT_TOKEN }}
    message: "Hello, this is a test message!"
    user_id: 1234
```

### Send a document to a channel in a community
```yaml
- name: Send a document to a channel in a community
  uses: New-dev0/switch-post-action@v1
  with:
    token: ${{ secrets.SWITCH_BOT_TOKEN }}
    message: "Hello, this is a test message!"
    document: "path/to/document.pdf"
    community_id: "123456"
    channel_id: "789012"
```
