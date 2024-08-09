import streamlit as st

def app():
    st.title("Comptabilité")
    st.write("Ici, vous pourrez gérer votre comptabilité.")
    st.write("Pour le moment, cette section est en construction.")
    st.write("Merci de votre compréhension.")

# Views setup
def views_compta():
    alma_view = st.Page(
        page="views/alma.py",
        title="Alma",
        icon="💳",
        default=True,
    )

    ebay_view = st.Page(
        page="views/ebay.py",
        title="eBay",
        icon="💳",
    )

    paypal_view = st.Page(
        page="views/paypal.py",
        title="PayPal",
        icon="💳",
    )

    payplug_view = st.Page(
        page="views/payplug.py",
        title="PayPlug",
        icon="💳",
    )

    # Navigation: Sidebar
    pg = st.navigation(
        {
            "Intégration": [alma_view, ebay_view, paypal_view, payplug_view],
            "Rapprochement comptable": [],
            "Autres...": [],
        }
    )

    # Run navigation
    pg.run()

# app()
views_compta()
