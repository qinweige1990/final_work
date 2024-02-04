import requests

headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LWF0LTEuY2VyIiwia2lkIjoiaW1zX25hMS1rZXktYXQtMSIsIml0dCI6ImF0In0.eyJpZCI6IjE3MDU5NzgxNTY3MDlfYzNhYmRmMDEtYzRiZC00OWNlLTgzY2MtOTU3MTY2Y2I5MmJhX3V3MiIsIm9yZyI6IjhGRTMxRDY2NjVBRTYyMDkwQTQ5NUNCN0BBZG9iZU9yZyIsInR5cGUiOiJhY2Nlc3NfdG9rZW4iLCJjbGllbnRfaWQiOiIyM2Q3Njg3MDZkODc0MDY3YTQ2YmYzMjg1YzNlZDdjNSIsInVzZXJfaWQiOiI4RTg5MUQ2QzY1QUU2MjMwMEE0OTVDRTRAdGVjaGFjY3QuYWRvYmUuY29tIiwiYXMiOiJpbXMtbmExIiwiYWFfaWQiOiI4RTg5MUQ2QzY1QUU2MjMwMEE0OTVDRTRAdGVjaGFjY3QuYWRvYmUuY29tIiwiY3RwIjozLCJtb2kiOiIzMDJmMWQ5NyIsImV4cGlyZXNfaW4iOiI4NjQwMDAwMCIsImNyZWF0ZWRfYXQiOiIxNzA1OTc4MTU2NzA5Iiwic2NvcGUiOiJvcGVuaWQsQWRvYmVJRCJ9.dfpAINkqzKJnwAmIjN1hMICkESG4GiI1RBdRBUiw8GyWL6YSyN9verWzmKzeEcc3qGR8bXo5lXySzB4AWlHxlzfuujUSyNVBRtvOllJZgYf4nunzwOib6HYz9l4MvpbtKLvyFuATVoZC-lxrvYL4Pa8ibT70_3BJ-C9dZLpXl6PQAZCtdMNeRuIptURizCOVsa_Cna58AD2Vu71Wjs1-mgLMFbUwN4b825M3wrLoCcTjvsIZhr4MCdPstV1oi85Bp7AuYTN6wO1kziqueAj185vMquZcVcxgMxU3rXP_PFI7qDcyWKmiiHPoagsCo6eFjryv6d7Cnt8P-i3lC1zhkg',
    'content-type': 'application/json',
    'x-api-key': '23d768706d874067a46bf3285c3ed7c5',
}

data = '{"input":{"href":"https://www.dropbox.com/scl/fi/ueelwkivu40rc4y4ugxr6/55658218-56c5-43fe-b621-42e0d0fc97e0_.png?rlkey=jdg19jg3gq03acl4azvml7axv&dl=0","storage":"dropbox"}, "output":{"href":"https://www.dropbox.com/request/PO7uE6VaiESRiU2QJXD8","storage":"dropbox","mask":{"format":"soft"}}}'

response = requests.post('https://image.adobe.io/sensei/cutout', headers=headers, data=data)
print(response.content)


curl --request POST \
               --url "https://image.adobe.io/sensei/cutout" \
                             --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LWF0LTEuY2VyIiwia2lkIjoiaW1zX25hMS1rZXktYXQtMSIsIml0dCI6ImF0In0.eyJpZCI6IjE3MDU5NzgxNTY3MDlfYzNhYmRmMDEtYzRiZC00OWNlLTgzY2MtOTU3MTY2Y2I5MmJhX3V3MiIsIm9yZyI6IjhGRTMxRDY2NjVBRTYyMDkwQTQ5NUNCN0BBZG9iZU9yZyIsInR5cGUiOiJhY2Nlc3NfdG9rZW4iLCJjbGllbnRfaWQiOiIyM2Q3Njg3MDZkODc0MDY3YTQ2YmYzMjg1YzNlZDdjNSIsInVzZXJfaWQiOiI4RTg5MUQ2QzY1QUU2MjMwMEE0OTVDRTRAdGVjaGFjY3QuYWRvYmUuY29tIiwiYXMiOiJpbXMtbmExIiwiYWFfaWQiOiI4RTg5MUQ2QzY1QUU2MjMwMEE0OTVDRTRAdGVjaGFjY3QuYWRvYmUuY29tIiwiY3RwIjozLCJtb2kiOiIzMDJmMWQ5NyIsImV4cGlyZXNfaW4iOiI4NjQwMDAwMCIsImNyZWF0ZWRfYXQiOiIxNzA1OTc4MTU2NzA5Iiwic2NvcGUiOiJvcGVuaWQsQWRvYmVJRCJ9.dfpAINkqzKJnwAmIjN1hMICkESG4GiI1RBdRBUiw8GyWL6YSyN9verWzmKzeEcc3qGR8bXo5lXySzB4AWlHxlzfuujUSyNVBRtvOllJZgYf4nunzwOib6HYz9l4MvpbtKLvyFuATVoZC-lxrvYL4Pa8ibT70_3BJ-C9dZLpXl6PQAZCtdMNeRuIptURizCOVsa_Cna58AD2Vu71Wjs1-mgLMFbUwN4b825M3wrLoCcTjvsIZhr4MCdPstV1oi85Bp7AuYTN6wO1kziqueAj185vMquZcVcxgMxU3rXP_PFI7qDcyWKmiiHPoagsCo6eFjryv6d7Cnt8P-i3lC1zhkg' \
                                      --header 'content-type: application/json' \
                                               --header 'x-api-key: 23d768706d874067a46bf3285c3ed7c5' \
                                                        --data '{"input":{"href":"https://www.dropbox.com/scl/fi/ueelwkivu40rc4y4ugxr6/55658218-56c5-43fe-b621-42e0d0fc97e0_.png?rlkey=jdg19jg3gq03acl4azvml7axv&dl=0","storage":"dropbox"},\
 "output":{"href":"https://www.dropbox.com/request/PO7uE6VaiESRiU2QJXD8","storage":"dropbox","mask":{"format":"soft"}}}'

curl --request GET \
               --url "https://image.adobe.io/pie/psdService/hello" \
                     --header "Authorization: Bearer eyJhbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LWF0LTEuY2VyIiwia2lkIjoiaW1zX25hMS1rZXktYXQtMSIsIml0dCI6ImF0In0.eyJpZCI6IjE3MDU5NzgxNTY3MDlfYzNhYmRmMDEtYzRiZC00OWNlLTgzY2MtOTU3MTY2Y2I5MmJhX3V3MiIsIm9yZyI6IjhGRTMxRDY2NjVBRTYyMDkwQTQ5NUNCN0BBZG9iZU9yZyIsInR5cGUiOiJhY2Nlc3NfdG9rZW4iLCJjbGllbnRfaWQiOiIyM2Q3Njg3MDZkODc0MDY3YTQ2YmYzMjg1YzNlZDdjNSIsInVzZXJfaWQiOiI4RTg5MUQ2QzY1QUU2MjMwMEE0OTVDRTRAdGVjaGFjY3QuYWRvYmUuY29tIiwiYXMiOiJpbXMtbmExIiwiYWFfaWQiOiI4RTg5MUQ2QzY1QUU2MjMwMEE0OTVDRTRAdGVjaGFjY3QuYWRvYmUuY29tIiwiY3RwIjozLCJtb2kiOiIzMDJmMWQ5NyIsImV4cGlyZXNfaW4iOiI4NjQwMDAwMCIsImNyZWF0ZWRfYXQiOiIxNzA1OTc4MTU2NzA5Iiwic2NvcGUiOiJvcGVuaWQsQWRvYmVJRCJ9.dfpAINkqzKJnwAmIjN1hMICkESG4GiI1RBdRBUiw8GyWL6YSyN9verWzmKzeEcc3qGR8bXo5lXySzB4AWlHxlzfuujUSyNVBRtvOllJZgYf4nunzwOib6HYz9l4MvpbtKLvyFuATVoZC-lxrvYL4Pa8ibT70_3BJ-C9dZLpXl6PQAZCtdMNeRuIptURizCOVsa_Cna58AD2Vu71Wjs1-mgLMFbUwN4b825M3wrLoCcTjvsIZhr4MCdPstV1oi85Bp7AuYTN6wO1kziqueAj185vMquZcVcxgMxU3rXP_PFI7qDcyWKmiiHPoagsCo6eFjryv6d7Cnt8P-i3lC1zhkg" \
                              --header "x-api-key: 23d768706d874067a46bf3285c3ed7c5"

curl --request POST \
               --url https://image.adobe.io/pie/psdService/documentManifest \
                             --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LWF0LTEuY2VyIiwia2lkIjoiaW1zX25hMS1rZXktYXQtMSIsIml0dCI6ImF0In0.eyJpZCI6IjE3MDU5ODE3ODc0MTVfYmM0ZTc5NjQtOTAzOS00YzI0LWE5ZGItYzFhOGQ4NWJjMzk4X3VlMSIsIm9yZyI6IjhGRTMxRDY2NjVBRTYyMDkwQTQ5NUNCN0BBZG9iZU9yZyIsInR5cGUiOiJhY2Nlc3NfdG9rZW4iLCJjbGllbnRfaWQiOiIyM2Q3Njg3MDZkODc0MDY3YTQ2YmYzMjg1YzNlZDdjNSIsInVzZXJfaWQiOiI4RTg5MUQ2QzY1QUU2MjMwMEE0OTVDRTRAdGVjaGFjY3QuYWRvYmUuY29tIiwiYXMiOiJpbXMtbmExIiwiYWFfaWQiOiI4RTg5MUQ2QzY1QUU2MjMwMEE0OTVDRTRAdGVjaGFjY3QuYWRvYmUuY29tIiwiY3RwIjozLCJtb2kiOiI5ZWJiNDU2OSIsImV4cGlyZXNfaW4iOiI4NjQwMDAwMCIsImNyZWF0ZWRfYXQiOiIxNzA1OTgxNzg3NDE1Iiwic2NvcGUiOiJvcGVuaWQsQWRvYmVJRCJ9.N598QSnISFXRuAMGX17uP8R3dfFv4RmkdtaddeCImoIXJ83f7196tAP-AkWUmfL-38Jx7ZGbd3CzQikh38Ef4BKK0paN7iQLDwVfbNghf1yrKoo0SC-wJoIsueryUcZ_8U39bLJspzvYfYLAiGYJrFd2SaOQghnsxxImAURuAOEMVMSuVpYTzlgXGoDYHuQEjj3rInxOoHsdAIT0SIHLOrkrYyOsuP9TFhlmZXz2VRZ-dJkv6EUUh9biUkwr3_gKxX_vDRBVXixeUL9c9CMT9UziWQxGQIYs2ZECITyjrKsgX8NeaWX3PSlCzOsM_ar71Jfl5zmW12-7zDDK9fDgLg' \
                                      --header 'content-type: application/json' \
                                               --header 'x-api-key: 23d768706d874067a46bf3285c3ed7c5' \
                                                        --data '{"inputs":[{"href":"get_presigned_url","storage":"external"}],\
 "options":{"thumbnails":{"type": "images/png"}}}'


curl --request POST \
               --url 'https://image.adobe.io/sensei/cutout' \
                     --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LWF0LTEuY2VyIiwia2lkIjoiaW1zX25hMS1rZXktYXQtMSIsIml0dCI6ImF0In0.eyJpZCI6IjE3MDU5NzgxNTY3MDlfYzNhYmRmMDEtYzRiZC00OWNlLTgzY2MtOTU3MTY2Y2I5MmJhX3V3MiIsIm9yZyI6IjhGRTMxRDY2NjVBRTYyMDkwQTQ5NUNCN0BBZG9iZU9yZyIsInR5cGUiOiJhY2Nlc3NfdG9rZW4iLCJjbGllbnRfaWQiOiIyM2Q3Njg3MDZkODc0MDY3YTQ2YmYzMjg1YzNlZDdjNSIsInVzZXJfaWQiOiI4RTg5MUQ2QzY1QUU2MjMwMEE0OTVDRTRAdGVjaGFjY3QuYWRvYmUuY29tIiwiYXMiOiJpbXMtbmExIiwiYWFfaWQiOiI4RTg5MUQ2QzY1QUU2MjMwMEE0OTVDRTRAdGVjaGFjY3QuYWRvYmUuY29tIiwiY3RwIjozLCJtb2kiOiIzMDJmMWQ5NyIsImV4cGlyZXNfaW4iOiI4NjQwMDAwMCIsImNyZWF0ZWRfYXQiOiIxNzA1OTc4MTU2NzA5Iiwic2NvcGUiOiJvcGVuaWQsQWRvYmVJRCJ9.dfpAINkqzKJnwAmIjN1hMICkESG4GiI1RBdRBUiw8GyWL6YSyN9verWzmKzeEcc3qGR8bXo5lXySzB4AWlHxlzfuujUSyNVBRtvOllJZgYf4nunzwOib6HYz9l4MvpbtKLvyFuATVoZC-lxrvYL4Pa8ibT70_3BJ-C9dZLpXl6PQAZCtdMNeRuIptURizCOVsa_Cna58AD2Vu71Wjs1-mgLMFbUwN4b825M3wrLoCcTjvsIZhr4MCdPstV1oi85Bp7AuYTN6wO1kziqueAj185vMquZcVcxgMxU3rXP_PFI7qDcyWKmiiHPoagsCo6eFjryv6d7Cnt8P-i3lC1zhkg' \
                              --header 'content-type: application/json' \
                                       --header 'x-api-key: 23d768706d874067a46bf3285c3ed7c5' \
                                                --data '{"input":{"href":"https://www.dropbox.com/scl/fi/ueelwkivu40rc4y4ugxr6/55658218-56c5-43fe-b621-42e0d0fc97e0_.png?rlkey=jdg19jg3gq03acl4azvml7axv&dl=0","storage":"dropbox"},"output":{"href":"https://www.dropbox.com/request/PO7uE6VaiESRiU2QJXD8","storage":"dropbox"}}'
