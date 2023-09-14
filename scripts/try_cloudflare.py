from pycloudflared import try_cloudflare

from modules.shared import cmd_opts
from helper import hm

from gradio import strings

import os

if cmd_opts.cloudflared:
    print("cloudflared detected, trying to connect...")
    port = cmd_opts.port if cmd_opts.port else 7860
    tunnel_url = try_cloudflare(port=port, verbose=False)
    os.environ['webui_url'] = tunnel_url.tunnel
    colab_url = os.getenv('colab_url')
    strings.en["SHARE_LINK_MESSAGE"] = f"Public WebUI Colab URL: {tunnel_url.tunnel}"
    strings.en["PUBLIC_SHARE_TRUE"] = f"Public WebUI Colab URL: {tunnel_url.tunnel}"
    print(f"Cloudflare WebUI Colab URL: {tunnel_url.tunnel}")
    servers = hm.server_infos if hm.server_infos else hm.get_server_info()
    for server in servers:
        hm.post_v2a(server["id"], "share_url: {}".format(tunnel_url.tunnel))

if cmd_opts.multiple:
    print("all detected, cloudflared trying to connect...")
    port = cmd_opts.port if cmd_opts.port else 7860
    tunnel_url = try_cloudflare(port=port, verbose=False)
    os.environ['webui_url'] = tunnel_url.tunnel
    colab_url = os.getenv('colab_url')
    strings.en["SHARE_LINK_MESSAGE"] = f"Public WebUI Colab URL: {tunnel_url.tunnel}"
    strings.en["PUBLIC_SHARE_TRUE"] = f"Public WebUI Colab URL: {tunnel_url.tunnel}"
    print(f"Cloudflare WebUI Colab URL: {tunnel_url.tunnel}")
    servers = hm.server_infos if hm.server_infos else hm.get_server_info()
    for server in servers:
        hm.post_v2a(server["id"], "share_url: {}".format(tunnel_url.tunnel))
