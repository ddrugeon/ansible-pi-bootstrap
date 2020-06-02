import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

def test_ssh_config(host):
    f = host.file('/etc/ssh/sshd_config')
    assert f.is_file
    assert f.exists
    assert f.contains('Port 22')
    assert f.contains('LoginGraceTime 2m')
    assert f.contains('PermitRootLogin no')
    assert f.contains('MaxAuthTries 6')
    assert f.contains('PubkeyAuthentication yes')
    assert f.contains('PasswordAuthentication no')
    assert f.contains('PermitEmptyPasswords no')
    assert f.contains('ChallengeResponseAuthentication no')
    assert f.contains('UsePAM no')
    assert f.contains('ClientAliveInterval  900')
    assert f.contains('ClientAliveCountMax 0')
    assert f.contains('AcceptEnv LANG LC_*')
    assert f.contains('AllowUsers admin')
