from pydantic import BaseModel, Field, AnyUrl
from typing import Annotated,Literal, Optional, List
from uuid import UUID
from datetime import datetime


class Product(BaseModel):  
     id: UUID
     sku: Annotated[str,Field(
           min_length=6,max_length=30,title="sku",description="Stock Keeping Unit,",example="SKU12345"
        )]
     name: Annotated[str,Field(
          min_length=3,max_length=80,title="product name",description="Name of product",example="[Samsung Galaxy S21,Apple iPhone 13]"
          )]
     description: Annotated[str,Field(
          max_length=200, description="Describe your product short"
          )]
     category:Annotated[str,Field(
          min_length=3,max_length=30,description="Category of the product like mobile , laptop",example="[Electronics,mobile,laptop]"
          )]
     brand:Annotated[str,Field(
          min_length=2,max_length=40,description="Brand of the product",example="[Samsung,Apple]"
          )]
     price:Annotated[float,Field(
            gt=0,strict=True,description="Price of the product(INR)",example=999.99
 )]
     currency:Literal["INR"] = "INR"
     discount_percent: Annotated[int,Field(ge=0,le=90,description="Discount in percent (0-90)",example=10)]=0
     stock: Annotated[int,Field(ge=0,description="Available stock (>=0)")]
     is_active:Annotated[bool,Field(description="Is the product active and available for sale?")] = True
     rating:Annotated[float,Field(ge=0,le=5,strict=True,description="RAting out of 5")]
     tags:Annotated[
          Optional[List[str]],
          Field(default=None,max_length=10,description="Upto to 10 tags",example=["smartphone","android","5g"])
          ]
     image_urls:Annotated[
            List[AnyUrl],
            Field(max_length=1,description="Image of the url")]
     #dimension
     #seller
     created_at : datetime