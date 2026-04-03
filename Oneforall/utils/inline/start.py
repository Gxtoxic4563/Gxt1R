from pyrogram.types import InlineKeyboardButton
import config
from Oneforall import app


# safe button function (NO CRASH)
def btn(text, **kwargs):
    try:
        return InlineKeyboardButton(
            text=text,
            icon_custom_emoji_id=6312260233171312151,
            **kwargs
        )
    except TypeError:
        return InlineKeyboardButton(
            text=text,
            **kwargs
        )


def start_panel(_):
    buttons = [
        [
            btn(_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"),
            btn(_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            btn(_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true")
        ],
        [
            btn(_["S_B_2"], url=config.SUPPORT_CHAT),
            btn(_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
        [
            btn(_["S_B_4"], callback_data="settings_back_helper")
        ],
        [
            btn(_["S_B_5"], url="https://t.me/docker_git_bit")
        ],
        [
            btn("✦ ᴡєʙ ɢᴧϻєꜱ 🎮✨", url="https://telegram-game-hub.vercel.app")
        ],
    ]
    return buttons