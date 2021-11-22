import json

string = '''
{
    "user": "Roo",
    "space": 100,
    "used": 20,
    "root":
    {
        "directories":
        [
            {
                "name": "folder1",
                "directories":
                [
                    {
                        "name": "subfolder1",
                        "directories": [],
                        "files": []
                    }
                ],
                "files":
                [
                    {
                        "name": "file1",
                        "extension": "txt",
                        "creation": "date",
                        "modification": "date",
                        "size": 5,
                        "path": "Roo/root/folder1/file1.txt",
                        "content": "hello world"
                    }
                ]
            },
            {
                "name": "folder2",
                "directories": [],
                "files": []
            }
        ],
        "files":
        [
            {
                "name": "file1",
                "extension": "txt",
                "creation": "date",
                "modification": "date",
                "size": 5,
                "path": "Roo/root/file1.txt",
                "content": "hello world"
            },
            {
                "name": "file2",
                "extension": "txt",
                "creation": "date",
                "modification": "date",
                "size": 5,
                "path": "Roo/root/file2.txt",
                "content": "hello world"
            }
        ]
    },
    "shared":
    {
        "directories":
        [
            {
                "name": "folder1",
                "directories": [],
                "files": []
            }
        ],
        "files":
        [
            {
                "name": "file1",
                "extension": "txt",
                "creation": "date",
                "modification": "date",
                "size": 5,
                "path": "Roo/shared/file1.txt",
                "content": "hello world"
            }
        ]
    }
}
'''

data = json.loads(string)
print(data["shared"]["files"][0]["content"])
