# ao.py
python sdk for ao https://ao.arweave.dev/

## install

```
```


## Example

```
import ao

# ao cred process id
CRED = 'Sa0iBLPNyJQrwpTTG-tWLQU-1QeUAJA73DdxGGiKoJc'
signer = ao.ARSigner('your ar wallet json file')

# use dry run to get your cred balance
result = ao.dry_run(signer, CRED, '', {'Action':'Balance'})
print(result)

# transfer
recipient = 'your recipient ar address'
message_id, result =ao.send_and_get(signer, CRED, '', {'Action':'Transfer', 'Recipient':recipient, 'Quantity':'1000'})
print(message_id)
print(result)
```
