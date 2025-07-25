# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024-07-17 10:49:26
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Base methods.
"""


from reykit.rbase import Base, Error, Exit


__all__ = (
    'BaseWeChat',
    'WeChatError',
    'WeChatClientErorr',
    'WeChatTriggerError',
    'WeChatTriggerContinueExit',
    'WeChatTriggerBreakExit'
)


class BaseWeChat(Base):
    """
    WeChat Base type.
    """


class WeChatError(BaseWeChat, Error):
    """
    WeChat error type.
    """


class WeChatExit(BaseWeChat, Exit):
    """
    WeChat exit type.
    """


class WeChatClientErorr(WeChatError):
    """
    WeChat client error type.
    """


class WeChatTriggerError(WeChatError):
    """
    WeChat trigger error type.
    """


class WeChatTriggerExit(WeChatExit):
    """
    WeChat trigger exit type.
    """


class WeChatTriggerContinueExit(WeChatTriggerExit):
    """
    WeChat trigger continue exit type.
    """


class WeChatTriggerBreakExit(WeChatTriggerExit):
    """
    WeChat trigger break exit type.
    """
