import pickle as pc
import streamlit as st
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

model = pc.load(open('estimasi_harga_mobil_bekas.sav', 'rb'))

# Set page title and favicon
st.set_page_config(page_title='Estimasi Harga Mobil Bekas', page_icon=':car:')

# Add a title and subtitle
st.title('Estimasi Harga Mobil Bekas')
st.markdown('Input parameter mobil untuk mendapatkan estimasi harga.')

# Add input fields for car parameters
year = st.number_input('Tahun Mobil', min_value=1900, max_value=2100, step=1)
mileage = st.number_input('KM Mobil', min_value=0, step=1000)
mpg = st.number_input('Konsumsi BBM Mobil', min_value=0.0, step=0.1)
tax = st.number_input('Pajak Mobil', min_value=0, step=1)
engineSize = st.number_input('Ukuran Mesin Mobil', min_value=0.0, step=0.1)

predict = ''

# Add button to estimate the price
if st.button('Estimasi Harga'):
    predict = model.predict([[year, mileage, mpg, tax, engineSize]])
    est_price_eur = predict[0]
    est_price_idr = est_price_eur * 16.824 * 1e6

    # Format the prices with fixed decimal places and without currency symbol
    est_price_eur_formatted = '{:,.2f}'.format(est_price_eur)
    est_price_idr_formatted = '{:,.2f}'.format(est_price_idr / 1e6)

    # Display the estimated prices with formatted text
    st.subheader('Hasil Estimasi Harga Mobil')
    st.write(f'Estimasi Harga Mobil Dalam EUR: {est_price_eur_formatted} EUR')
    st.write(f'Estimasi Harga Mobil Dalam Rupiah (Juta): {est_price_idr_formatted} Juta IDR')
