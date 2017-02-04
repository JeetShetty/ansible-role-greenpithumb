# Ansible Role: GreenPiThumb

[![Build Status](https://travis-ci.org/JeetShetty/ansible-role-greenpithumb.svg?branch=master)](https://travis-ci.org/JeetShetty/ansible-role-greenpithumb)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-greenpithumb-blue.svg?style=flat-square)](https://galaxy.ansible.com/JeetShetty/greenpithumb)
[![License](http://img.shields.io/:license-apache-blue.svg?style=flat-square)](LICENSE)

Ansible role for [GreenPiThumb](https://github.com/JeetShetty/greenpithumb).

## Role Variables

Available variables are listed below, along with default values (see [defaults/main.yml](defaults/main.yml)):

```yaml
greenpithumb_backend_user: greenpithumb
greenpithumb_backend_group: greenpithumb
```

The user and group under which to run GreenPiThumb.

```yaml
greenpithumb_backend_path: "/opt/greenpithumb"
```

The path to which to install the GreenPiThumb backend files.

```yaml
greenpithumb_git_version: "master"
```

The source git version/branch to install GreenPiThumb.

```yaml
greenpithumb_git_repo: "https://github.com/JeetShetty/GreenPiThumb"
```

The git repository to use for GreenPiThumb.

## Dependencies

* [geerlingguy.nginx](https://galaxy.ansible.com/geerlingguy/nginx/)

## Example Playbook

#### `example.yml`

```yaml
- hosts: all
  roles:
    - { role: JeetShetty.greenpithumb }
```

### Running Example Playbook

```shell
ansible-galaxy install JeetShetty.greenpithumb
ansible-playbook example.yml
```

## License

Apache2

## Author Information

This role was created in 2017 by [Jeet Shetty](https://github.com/JeetShetty) and [Michael Lynch](http://mtlynch.io).
