import logging
import streamlit as st
from database.init_db import initialize_database
from frontend.checkout_and_ops import (
    render_cart_and_checkout_page,
    render_operations_dashboard,
    render_order_confirmation_page,
)
from frontend.components import inject_custom_css, render_footer, render_header
from frontend.seller_portal import (
    render_customer_registration_page,
    render_shop_registration_page,
)
from frontend.store_views import (
    render_catalogue_page,
    render_home_page,
    render_product_details_page,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

st.set_page_config(
    page_title="BharatKart — Curated Multi-City Commerce",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


@st.cache_resource
def bootstrap_app() -> bool:
    initialize_database()
    return True


def main() -> None:
    bootstrap_app()
    inject_custom_css()
    current_city = render_header()

    page = st.session_state.get("active_page", "Home")
    if page == "Home":
        render_home_page(current_city)
    elif page == "Catalogue":
        render_catalogue_page(current_city)
    elif page == "ProductDetails":
        render_product_details_page(current_city)
    elif page == "RegisterShop":
        render_shop_registration_page(current_city)
    elif page == "CustomerRegister":
        render_customer_registration_page(current_city)
    elif page == "Cart":
        render_cart_and_checkout_page(current_city)
    elif page == "OrderConfirmation":
        render_order_confirmation_page()
    elif page == "Operations":
        render_operations_dashboard()
    else:
        render_home_page(current_city)

    render_footer()


if __name__ == "__main__":
    main()
