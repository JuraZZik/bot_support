#!/usr/bin/env python3
"""
Centralized locale helper utility

Provides single point for locale management across the bot.
Eliminates code duplication and ensures consistency.
"""

import logging
from typing import Optional
from config import DEFAULT_LOCALE, ADMIN_ID
from locales import get_user_locale, set_user_locale as locales_set_user_locale
from storage.data_manager import data_manager

logger = logging.getLogger(__name__)


def get_user_language(user_id: int) -> str:
    """
    Get user language with fallback chain:
    1. User-specific locale (from memory cache)
    2. User data from storage (persistent)
    3. Default locale from config

    Args:
        user_id: Telegram user ID

    Returns:
        Language code (e.g., 'ru', 'en')
    """
    try:
        # Try memory cache first (fastest)
        lang = get_user_locale(user_id)
        if lang:
            return lang

        # Try storage (persistent)
        user_data = data_manager.get_user_data(user_id)
        lang = user_data.get("locale")
        if lang:
            locales_set_user_locale(user_id, lang)
            return lang
    except Exception as e:
        logger.warning(f"Failed to load user locale for {user_id}: {e}")

    # Fallback to default
    return DEFAULT_LOCALE


def get_admin_language() -> str:
    """
    Get admin language from storage

    Returns:
        Admin's language code or default
    """
    try:
        admin_data = data_manager.get_user_data(ADMIN_ID)
        lang = admin_data.get("locale", DEFAULT_LOCALE)
        return lang
    except Exception as e:
        logger.warning(f"Failed to load admin locale: {e}")
        return DEFAULT_LOCALE


def set_user_language(user_id: int, lang_code: str) -> bool:
    """
    Set user language with persistence

    Args:
        user_id: Telegram user ID
        lang_code: Language code (ru, en, etc.)

    Returns:
        True if successful, False otherwise
    """
    try:
        locales_set_user_locale(user_id, lang_code)
        data_manager.update_user_data(user_id, {"locale": lang_code})
        logger.info(f"Set language for user {user_id}: {lang_code}")
        return True
    except Exception as e:
        logger.error(f"Failed to set language for user {user_id}: {e}")
        return False
