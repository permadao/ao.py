import requests
import arseeding
from .signer import ARSigner

SDK = 'ao.py'
MU = 'https://mu.ao-testnet.xyz'
CU = 'https://cu.ao-testnet.xyz'
SCHEDULER = '_GQ33BkPtZrqxA84vM8Zk-N2aO0toNNu_C-l-rawrBA'

def send_message(singer, pid, anchor, tags, data='', mu=MU, timeout=5):
    default_tags = {
        'Data-Protocol': 'ao',
        'Variant': 'ao.TN.1',
        'Type': 'Message',
        'SDK': SDK,
    }
    default_tags.update(tags)
    b = arseeding.BundleItem(singer, pid, anchor, default_tags, data)
    return b.id, requests.post(mu, data=b.binary, headers={'Content-Type': 'application/octet-stream'}, timeout=timeout).json()


def dry_run(pid, anchor, tags, data='', cu=CU, timeout=30):
    default_tags = {
        'Data-Protocol': 'ao',
        'Variant': 'ao.TN.1',
        'Type': 'Message',
        'SDK': SDK,
    }
    default_tags.update(tags)

    tags = [{'name':k, 'value':v} for k,v in tags.items()]
    url = '%s/dry-run?process-id=%s' % (cu, pid)
    payload = {
        'Target': pid,
        'Owner': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
        'Anchor': anchor,
        'Data': data,
        'Tags': tags,
    }
    return requests.post(url, json=payload, timeout=timeout).json()
    
def spawn_process(singer, module, anchor, tags, data='', mu=MU, scheduler=SCHEDULER, timeout=5):
    default_tags = {
        'Data-Protocol': 'ao',
        'Variant': 'ao.TN.1',
        'Type': 'Process',
        'Scheduler':scheduler,
        'Module':module,
        'SDK': SDK,
    }
    default_tags.update(tags)
    b = arseeding.BundleItem(singer, '', anchor, default_tags, data)
    return b.id, requests.post(mu, data=b.binary, headers={'Content-Type': 'application/octet-stream'}, timeout=timeout).json()

def get_result(pid, message_id, cu=CU, timeout=5):
    return requests.get(f'{cu}/result/{message_id}?process-id={pid}', timeout=timeout).json()

def send_and_get(singer, pid, anchor, tags, data='', mu=MU, cu=CU, timeout=5):
    mid, _ = send_message(singer, pid, anchor, tags, data, mu, timeout)
    return mid, get_result(pid, mid, cu, timeout)
