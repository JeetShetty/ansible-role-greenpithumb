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

The user and group under which to run the GreenPiThumb backend service.

```yaml
greenpithumb_backend_path: "/opt/greenpithumb"
```

The path to which to install the GreenPiThumb backend files.

```yaml
greenpithumb_frontend_user: greenpithumb-frontend
greenpithumb_frontend_group: greenpithumb-frontend
```

The user and group under which to run the GreenPiThumb frontend web server.

```yaml
greenpithumb_frontend_path: "/opt/greenpithumb-frontend"
```

The path to which to install the GreenPiThumb frontend files.

```yaml
greenpithumb_frontend_web_port: 80
```

The port the GreenPiThumb web app will listen to for external HTTP requests.

```yaml
greenpithumb_diagnostics_enabled: True
```

Controls whether to install simple scripts for diagnosing GreenPiThumb's
hardware.

```yaml
greenpithumb_diagnostic_path: "/opt/greenpithumb-diagnostic"
```

Path to install GreenPiThumb's diagnostic scripts.

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
