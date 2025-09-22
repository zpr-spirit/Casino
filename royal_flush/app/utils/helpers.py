"""
Helper utility functions
"""
from typing import Any, Dict, List, Optional
from datetime import datetime, date
import json
import random
import string

def generate_id(length: int = 8) -> str:
    """
    Generate random ID
    
    Args:
        length: ID length
        
    Returns:
        str: Random ID
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def format_currency(amount: float, currency: str = "¥") -> str:
    """
    Format currency
    
    Args:
        amount: Amount
        currency: Currency symbol
        
    Returns:
        str: Formatted currency string
    """
    if amount >= 1e8:
        return f"{currency}{amount/1e8:.2f}B"
    elif amount >= 1e4:
        return f"{currency}{amount/1e4:.2f}W"
    else:
        return f"{currency}{amount:.2f}"

def format_percentage(value: float, decimals: int = 2) -> str:
    """
    Format percentage
    
    Args:
        value: Value
        decimals: Decimal places
        
    Returns:
        str: Formatted percentage string
    """
    return f"{value:.{decimals}f}%"

def safe_json_loads(json_str: str, default: Any = None) -> Any:
    """
    Safe JSON parsing
    
    Args:
        json_str: JSON string
        default: Default value
        
    Returns:
        Any: Parsed result or default value
    """
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, TypeError):
        return default

def safe_json_dumps(obj: Any, default: str = "{}") -> str:
    """
    Safe JSON serialization
    
    Args:
        obj: Object to serialize
        default: Default value
        
    Returns:
        str: JSON string
    """
    try:
        return json.dumps(obj, ensure_ascii=False, default=str)
    except (TypeError, ValueError):
        return default

def validate_date_range(start_date: str, end_date: str) -> bool:
    """
    Validate date range
    
    Args:
        start_date: Start date
        end_date: End date
        
    Returns:
        bool: Whether valid
    """
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()
        return start <= end
    except ValueError:
        return False

def calculate_days_between(start_date: str, end_date: str) -> int:
    """
    Calculate days between two dates
    
    Args:
        start_date: Start date
        end_date: End date
        
    Returns:
        int: Days difference
    """
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()
        return (end - start).days
    except ValueError:
        return 0

def clean_string(text: str) -> str:
    """
    Clean string
    
    Args:
        text: Original string
        
    Returns:
        str: Cleaned string
    """
    if not text:
        return ""
    
    # Remove leading/trailing spaces
    text = text.strip()
    
    # Remove extra whitespace
    text = " ".join(text.split())
    
    return text

def mask_sensitive_data(data: str, mask_char: str = "*", visible_chars: int = 4) -> str:
    """
    Mask sensitive data
    
    Args:
        data: Original data
        mask_char: Mask character
        visible_chars: Visible character count
        
    Returns:
        str: Masked data
    """
    if not data or len(data) <= visible_chars:
        return data
    
    return data[:visible_chars] + mask_char * (len(data) - visible_chars)

def paginate_list(items: List[Any], page: int, size: int) -> Dict[str, Any]:
    """
    Paginate list
    
    Args:
        items: Item list
        page: Page number (starting from 1)
        size: Page size
        
    Returns:
        Dict[str, Any]: Pagination result
    """
    total = len(items)
    start = (page - 1) * size
    end = start + size
    
    paginated_items = items[start:end]
    total_pages = (total + size - 1) // size
    
    return {
        "items": paginated_items,
        "total": total,
        "page": page,
        "size": size,
        "pages": total_pages,
        "has_next": page < total_pages,
        "has_prev": page > 1
    }
