import streamlit as st

# shop items
shop = [
    {'id': 1, 'product_name': 'Salt', 'price': 250, 'quantity': 150},
    {'id': 2, 'product_name': 'Sugar', 'price': 200, 'quantity': 100},
    {'id': 3, 'product_name': 'Oil', 'price': 550, 'quantity': 200},
    {'id': 4, 'product_name': 'Flour', 'price': 150, 'quantity': 1000},
    {'id': 5, 'product_name': 'Milk', 'price': 250, 'quantity': 50},
    {'id': 6, 'product_name': 'Shampoo', 'price': 450, 'quantity': 10},
    {'id': 7, 'product_name': 'Toothpaste', 'price': 250, 'quantity': 50},
    {'id': 8, 'product_name': 'Eggs', 'price': 35, 'quantity': 120},
    {'id': 9, 'product_name': 'Lays', 'price': 100, 'quantity': 100},
    {'id': 10, 'product_name': 'Soap', 'price': 50, 'quantity': 20},
]

# Initialize the cart
if "cart" not in st.session_state:
    st.session_state.cart = []

# Backend Logic
def show_products():
    st.subheader("**Available Products**")
    st.write('---------------------------------------------')
    for product in shop:
        st.markdown(
            f"""
            ● ID: {product['id']}  
            📦 Product: {product['product_name']}  
            💵 Price: Rs {product['price']}  
            📈 Stock: {product['quantity']}
            """
        )

def add_to_cart(cart, product_id, quantity):
    for product in shop:
        if product['id'] == product_id:
            if quantity <= product['quantity']:
                cart.append({
                    'id': product['id'],
                    'product_name': product['product_name'],
                    'price': product['price'],
                    'quantity': quantity
                })
                product['quantity'] -= quantity
                st.success(f"{quantity} × {product['product_name']} added to cart!")
                return
            else:
                st.error("Not enough stock available")
                return
    st.error("Invalid Product ID")

def view_cart(cart):
    st.subheader("🛒 Your Cart")
    if not cart:
        st.info("Cart is empty")
        return

    for item in cart:
        st.write(f"{item['product_name']}(x{item['quantity']}) - Rs: {item['price'] * item['quantity']}")

def remove_from_cart(cart, product_id):
    for item in cart:
        if item['id'] == product_id:
            cart.remove(item)
            st.success("Item removed from cart")
            return
    st.error("Item not found in cart")

def calculate_total(cart):
    total = 0
    for item in cart:
        total += item['price'] * item['quantity']
    return total

def checkout(cart):
    if not cart:
        st.warning("Cart is empty")
        return
    total = calculate_total(cart)
    st.success(f"Order Placed Successfully!")
    st.subheader(f"Total Bill: Rs {total}")
    cart.clear()

# Frontend Logic
st.set_page_config(page_title="Online Shop", page_icon="🛒")
st.title("Online Shop System")
st.caption("Welcome to our Online shoping system!")

menu = st.sidebar.selectbox(
    "Main Menu",
    ["View Products", "Add to Cart", "View Cart", "Remove Item", "Checkout"]
)

if menu == "View Products":
    show_products()

elif menu == "Add to Cart":
    st.subheader("Add Product to Cart")

    product = st.number_input("Enter Product ID", min_value=1, step=1)
    quantity = st.number_input("Enter Quantity", min_value=1, step=1)

    if st.button("Add"):
        add_to_cart(st.session_state.cart, product, quantity)

elif menu == "View Cart":
    view_cart(st.session_state.cart)
    st.subheader(f"Total: Rs {calculate_total(st.session_state.cart)}")

elif menu == "Remove Item":
    st.subheader("Remove Product from Cart")
    product = st.number_input("Enter Product ID to Remove", min_value=1, step=1)
    if st.button("Remove"):
        remove_from_cart(st.session_state.cart, product)

elif menu == "Checkout":
    checkout(st.session_state.cart)