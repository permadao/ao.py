# ao.py
python sdk for ao https://ao.arweave.dev/

## install

```
pip install aodotpy
```


## Example

```
import ao

# ao cred process id
ar = 'xU9zFkq3X2ZQ6olwNVvr1vUWIjc3kXTWr7xKQD6dh10'
signer = ao.ARSigner('your ar wallet json file')

# use dry run to get your cred balance
result = ao.dry_run(signer, ar, '', {'Action':'Balance'})
print(result)

# transfer
recipient = 'your recipient ar address'
message_id, result =ao.send_and_get(signer, ar, '', {'Action':'Transfer', 'Recipient':recipient, 'Quantity':'1000000000000'})
print(message_id)
print(result)
```
