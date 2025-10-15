"""
Collections API - Money collection from customers via mobile money
"""

import re
import uuid
from typing import Dict, Any, Optional

from ..errors import MarzPayError


class CollectionsAPI:
    """
    Collections API - Money collection from customers via mobile money
    
    This class handles all collection-related operations including:
    - Initiating money collections
    - Retrieving collection details
    - Getting available collection services
    
    Example:
        ```python
        client = MarzPay(config)
        
        # Collect money from customer
        result = client.collections.collect_money(
            amount=5000,
            phone_number="0759983853",
            reference="550e8400-e29b-41d4-a716-446655440000",
            description="Payment for services"
        )
        ```
    """

    def __init__(self, client):
        """Initialize CollectionsAPI with MarzPay client"""
        self.client = client

    def collect_money(
        self,
        amount: int,
        phone_number: str,
        reference: str,
        description: Optional[str] = None,
        callback_url: Optional[str] = None,
        country: str = "UG",
    ) -> Dict[str, Any]:
        """
        Collect money from a customer via mobile money
        
        Args:
            amount: Amount in UGX (500-10,000,000)
            phone_number: Customer's phone number
            reference: Unique UUID4 reference for the transaction
            description: Payment description (optional)
            callback_url: Custom webhook URL (optional)
            country: Country code (default: UG)
        
        Returns:
            Collection result with transaction details
            
        Raises:
            MarzPayError: When validation fails or API request fails
            
        Example:
            ```python
            try:
                result = client.collections.collect_money(
                    amount=10000,
                    phone_number="0759983853",
                    reference=client.collections.generate_reference(),
                    description="Payment for services"
                )
                
                print(f"Collection ID: {result['data']['collection_id']}")
            except MarzPayError as e:
                print(f"Error: {e.message}")
            ```
        """
        params = {
            "amount": amount,
            "phone_number": phone_number,
            "reference": reference,
            "description": description,
            "callback_url": callback_url,
            "country": country,
        }

        self._validate_collect_money_params(params)

        # Format phone number
        params["phone_number"] = self._format_phone_number(phone_number)

        return self.client.request(
            "/collections",
            method="POST",
            data=params,
        )

    def get_collection(self, collection_id: str) -> Dict[str, Any]:
        """
        Get collection details by ID
        
        Args:
            collection_id: Collection ID
            
        Returns:
            Collection details
            
        Raises:
            MarzPayError: When request fails
        """
        if not collection_id:
            raise MarzPayError.validation_error("Collection ID is required")

        return self.client.request(f"/collections/{collection_id}")

    def get_collections(
        self,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        status: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Get all collections with optional filters
        
        Args:
            page: Page number
            limit: Items per page
            status: Filter by status
            from_date: Filter from date (YYYY-MM-DD)
            to_date: Filter to date (YYYY-MM-DD)
            
        Returns:
            Collections list
        """
        filters = {}
        
        if page is not None:
            filters["page"] = page
        if limit is not None:
            filters["limit"] = limit
        if status is not None:
            filters["status"] = status
        if from_date is not None:
            filters["from_date"] = from_date
        if to_date is not None:
            filters["to_date"] = to_date

        endpoint = "/collections"
        if filters:
            query_params = "&".join([f"{k}={v}" for k, v in filters.items()])
            endpoint += f"?{query_params}"

        return self.client.request(endpoint)

    def get_services(self) -> Dict[str, Any]:
        """
        Get available collection services
        
        Returns:
            Available services
        """
        return self.client.request("/collections/services")

    def generate_reference(self) -> str:
        """
        Generate a unique reference for collections
        
        Returns:
            UUID4 reference string
        """
        return str(uuid.uuid4())

    def _validate_collect_money_params(self, params: Dict[str, Any]) -> None:
        """
        Validate collect money parameters
        
        Args:
            params: Parameters to validate
            
        Raises:
            MarzPayError: When validation fails
        """
        errors = []

        # Validate amount
        amount = params.get("amount")
        if amount is None:
            errors.append("Amount is required")
        elif not isinstance(amount, int):
            errors.append("Amount must be an integer")
        elif amount < 500:
            errors.append("Amount must be at least 500 UGX")
        elif amount > 10000000:
            errors.append("Amount must not exceed 10,000,000 UGX")

        # Validate phone number
        phone_number = params.get("phone_number")
        if not phone_number:
            errors.append("Phone number is required")

        # Validate reference
        reference = params.get("reference")
        if not reference:
            errors.append("Reference is required")

        if errors:
            raise MarzPayError.validation_error(
                "Validation failed", {"validation_errors": errors}
            )

    def _format_phone_number(self, phone_number: str) -> str:
        """
        Format phone number for API
        
        Args:
            phone_number: Phone number to format
            
        Returns:
            Formatted phone number
        """
        # Remove any non-digit characters
        phone_number = re.sub(r"[^0-9]", "", phone_number)
        
        # Add country code if not present
        if not phone_number.startswith("256"):
            if phone_number.startswith("0"):
                phone_number = "256" + phone_number[1:]
            else:
                phone_number = "256" + phone_number

        return phone_number

