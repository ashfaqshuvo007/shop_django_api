## Idea

Chat module is consists of three major components:
* Chat thread
* chat inbox, and
* chat message

#### Chat Thread
Chat thread is communication thread between two or more users.

#### Chat Inbox
A chat thread contains two or more chat inbox. An inbox is the copy of the chat for a participants.
Each user has own inbox, so that they can delete message from their own copy of inbox.

#### Chat Message
Each individual message. Each message is cloned in each of the inboxes of the thread.

## API Reference

#### To get the list of all threads:

*GET `/chats/threads/`*

Sample Response:
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "tsync_id": "a0bb6425-c0c3-4da6-aebd-87610294f71f",
            "reference_order": null,
            "last_updated": "2019-10-09T18:06:35.921656Z",
            "date_created": "2019-10-09T18:06:35.920687Z",
            "thread_chat_inboxes": [
                {
                    "id": 4,
                    "tsync_id": "902a6334-c8c0-4eb9-8175-6a8f03b969a3",
                    "chat_thread": 3,
                    "user": 2
                },
                {
                    "id": 3,
                    "tsync_id": "625f1157-82d8-4bf0-b89f-ce1737106be0",
                    "chat_thread": 3,
                    "user": 1
                }
            ],
            "participants": [
                2,
                1
            ]
        }
    ]
}
```

#### To create a new chat thread

*POST `/chats/threads/`*

Request body:
```json
{
	"tsync_id": "abcferere",
	"participants": [1,2]
}
```

You can also provide reference order in the request body too:
```json
{
	"tsync_id": "abcferere",
	"participants": [1,2],
    "reference_order": 2
}
```

Note that, here participants in the list of user ids for this chat thread.

### To submit a new message by a user

*POST `/chats/messages/`*

Request body:
```json
{
	"chat_thread": 3,
	"text": "This is a test message",
	"sent_by": 1,
	"tsync_id": "tdfdklf-fdff-fdfd"
}
```

### To retrieve latest messages of a thread:

*GET `/chats/messages/?chat_thread=<thread-id>`*

Sample response:
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "tsync_id": "13dc9c70-7f4a-41dc-a772-b288f61e9b2d",
            "text": "This is a test message",
            "chat_thread": 3,
            "sent_by": 1
        }
    ]
}
```

For next (older) batch of messages:
*GET `/chats/messages/?chat_thread=<thread-id>&last_message=<smallest-pk>`*

and so on. Continue until there is no more messages are returned.