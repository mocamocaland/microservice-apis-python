from typing import Any, Dict, Optional
import uuid
from datetime import datetime
from uuid import UUID
from fastapi import HTTPException
from starlette import status
from starlette.responses import Response
from app import app
from api.schemas import (
    GetOrderSchema,
    CreateOrderSchema,
    GetOrdersSchema
)

# テストデータ
orders = []
# orders = [
#     {
#         'id': 'ff0f1355-e821-4178-9567-550dec27a373',
#         'status': "delivered",
#         'created': datetime.utcnow(),
#         'order': [
#             {
#                 'product': 'cappuccino',
#                 'size': 'medium',
#                 'quantity': 1
#             }
#         ]
#     },
#     {
#         'id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
#         'status': "paid",
#         'created': datetime.utcnow(),
#         'order': [
#             {
#                 'product': 'coffee',
#                 'size': 'medium',
#                 'quantity': 1
#             },
#             {
#                 'product': 'espresso',
#                 'size': 'small',
#                 'quantity': 2
#             }
#         ]
#     }
# ]


# OrdersAPI
@app.get('/orders', response_model=GetOrdersSchema)
def get_orders(cancelled: Optional[bool] = None, limit: Optional[int] = None) -> dict[str, list[dict[str, Any]]]:
    if cancelled is None and limit is None:
        return {'orders': orders}
    query_set = [order for order in orders]

    if cancelled is not None:
        if cancelled:
            query_set = [
                order
                for order in query_set
                if order['status'] == 'cancelled'
            ]
        else:
            query_set = [
                order
                for order in query_set
                if order['status'] != 'cancelled'
            ]
    if limit is not None and len(query_set) > limit:
        return {'orders': query_set[:limit]}

    return {'orders': query_set}


@app.post(
    '/orders',
    status_code=status.HTTP_201_CREATED,
    response_model=GetOrderSchema
)
def create_order(order: CreateOrderSchema) -> Any:
    order = order.dict()
    order["id"] = uuid.uuid4()
    order["created"] = datetime.utcnow()
    order["status"] = "created"
    orders.append(order)
    return order


@app.get('/orders/{order_id}', response_model=GetOrderSchema)
def get_order(order_id: UUID) -> dict[str, Any]:
    for order in orders:
        if order["id"] == order_id:
            return order
    raise HTTPException(
        status_code=404,
        detail=f"Order with ID {order_id} not found"
    )


@app.put('/orders/{order_id}', response_model=GetOrderSchema)
def update_order(
            order_id: UUID,
            order_details: CreateOrderSchema
        ) -> Dict[str, Any]:
    for order in orders:
        if order["id"] == order_id:
            order.update(order_details)
            # order.update(order_details.Dict())
            return order
    raise HTTPException(
        status_code=404,
        detail=f"Order with ID {order_id} not found"
    )


@app.delete(
    '/orders/{order_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
)
def delete_order(order_id: UUID) -> None:
    for index, order in enumerate(orders):
        if order["id"] == order_id:
            orders.pop(index)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Order with ID {order_id} not found"
    )


@app.post('/orders/{order_id}/cancel', response_model=GetOrderSchema)
def cancel_order(order_id: UUID) -> dict[str, Any]:
    for order in orders:
        if order["id"] == order_id:
            order["status"] = "cancelled"
            return order
    raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found")


@app.post('/orders/{order_id}/pay', response_model=GetOrderSchema)
def pay_order(order_id: UUID) -> dict[str, Any]:
    for order in orders:
        if order["id"] == order_id:
            order["status"] = "paid"
            return order
    raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found")
