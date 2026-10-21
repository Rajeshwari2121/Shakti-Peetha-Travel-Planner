import math
import re
from pathlib import Path
from urllib.parse import quote

import pandas as pd
import requests
import streamlit as st

st.set_page_config(page_title="Shakti Peetha Yatra", page_icon="🛕", layout="wide")

st.markdown("""
<style>
.stApp {background: #fff9f2;}
[data-testid="stSidebar"] {background: linear-gradient(180deg,#64172f,#a34153);}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {color:white !important;}
.hero {padding:35px; border-radius:22px; color:white;
 background:linear-gradient(115deg,#681630,#aa3850,#d99b4d);
 box-shadow:0 10px 25px #6b223322; margin-bottom:20px;}
.hero h1 {color:white!important; font-size:42px; margin:0;}
.hero p {color:#fff0dc; font-size:17px;}
.tile {background:white; border:1px solid #efd9cf; padding:19px;
 border-radius:16px; margin:8px 0; min-height:100px;
 box-shadow:0 4px 14px #64223812; overflow-wrap:anywhere;}
.tile strong {color:#812841;}
[data-testid="stMetric"] {background:white; border-radius:14px;
 border:1px solid #ecd8cd; padding:12px;}
</style>
""", unsafe_allow_html=True)

APP_DIR = Path(__file__).resolve().parent
PREFERRED_CSV = APP_DIR / "Ashtadasha_18_Shakti_Peethas_Final_No_Blanks.csv"
all_csvs = sorted(APP_DIR.glob("*.csv"))
if PREFERRED_CSV.exists():
    csv_path = PREFERRED_CSV
elif len(all_csvs) == 1:
    csv_path = all_csvs[0]
elif all_csvs:
    csv_path = st.sidebar.selectbox("Choose dataset", all_csvs, format_func=lambda p: p.name)
else:
    st.error("No CSV file found alongside Shakti_Peetha_Travel_App.py")
    st.code(str(APP_DIR))
    st.stop()

try:
    df = pd.read_csv(csv_path, keep_default_na=False, encoding="utf-8-sig")
except Exception as exc:
    st.error(f"Could not read CSV: {exc}")
    st.stop()
df.columns = df.columns.astype(str).str.strip()
if df.empty:
    st.error("CSV is empty.")
    st.stop()

def column(*words):
    for c in df.columns:
        if all(w.lower() in c.lower() for w in words):
            return c
    return None

NAME = column("shakti", "name") or column("temple", "name")
if not NAME:
    st.error("Temple name column missing. Available columns:")
    st.write(df.columns.tolist())
    st.stop()

def value(row, *words):
    c = column(*words)
    if not c:
        return "Not available"
    v = str(row[c]).strip()
    return v if v else "Not available"

def fields(row, keys):
    matched = [c for c in df.columns if any(k in c.lower() for k in keys)]
    if not matched:
        st.info("No matching fields in the dataset.")
    for i in range(0, len(matched), 2):
        cols = st.columns(2)
        for j, c in enumerate(matched[i:i+2]):
            with cols[j]:
                with st.container(border=True):
                    st.caption(c)
                    st.write(str(row[c]) or "Not available")

def number_from_text(text):
    m = re.search(r"\d+(?:,\d{3})*(?:\.\d+)?", str(text))
    return float(m.group().replace(",", "")) if m else None

def map_link(query):
    return "https://www.google.com/maps/search/?api=1&query=" + quote(query)

@st.cache_data(ttl=3600, show_spinner=False)
def commons_images(search):
    try:
        response = requests.get(
            "https://commons.wikimedia.org/w/api.php",
            params={"action":"query", "generator":"search", "gsrsearch":search,
                    "gsrnamespace":6, "gsrlimit":10, "prop":"imageinfo",
                    "iiprop":"url", "iiurlwidth":500, "format":"json"},
            headers={"User-Agent":"ShaktiPeethaYatraEducationalApp/1.0 (local use)"},
            timeout=12)
        response.raise_for_status()
        results = []
        for p in response.json().get("query",{}).get("pages",{}).values():
            info = p.get("imageinfo",[])
            if info:
                img = info[0]
                url = img.get("thumburl") or img.get("url")
                if url:
                    results.append((url,p.get("title",""),img.get("descriptionurl","")))
        return results
    except (requests.RequestException, ValueError):
        return []

IMAGE_TERMS = {
    "shankari":"Koneswaram Temple Trincomalee",
    "kamakshi":"Kamakshi Amman Temple Kanchipuram",
    "shrinkhala":"Shrinkhala Devi Pandua",
    "chamunda":"Chamundeshwari Temple Mysore",
    "jogulamba":"Jogulamba Temple Alampur",
    "bhramaramba":"Bhramaramba Temple Srisailam",
    "mahalakshmi":"Mahalakshmi Temple Kolhapur",
    "ekaveerika":"Renuka Devi Mahur Temple",
    "mahakali":"Harsiddhi Temple Ujjain",
    "puruhutika":"Puruhutika Temple Pithapuram",
    "girija":"Biraja Temple Jajpur",
    "biraja":"Biraja Temple Jajpur",
    "manikyamba":"Manikyamba Temple Draksharamam",
    "kamakhya":"Kamakhya Temple Guwahati",
    "madhaveswari":"Alopi Devi Temple Prayagraj",
    "jwalamukhi":"Jwala Devi Temple Kangra",
    "vaishnavi":"Jwala Devi Temple Kangra",
    "mangala gauri":"Mangala Gauri Temple Gaya",
    "vishalakshi":"Vishalakshi Temple Varanasi",
    "sharada":"Sharada Peeth Kashmir",
    "saraswati":"Sharada Peeth Kashmir"
}

def open_temple(temple_index=None):
    """Navigate before widgets are instantiated on the next Streamlit rerun."""
    st.session_state["navigation"] = "🛕 Temple Explorer"
    if temple_index is not None:
        st.session_state["selected_temple_index"] = temple_index


st.sidebar.title("🛕 Shakti Peetha Yatra")
st.sidebar.caption("Your local pilgrimage companion")
page = st.sidebar.radio("Navigation", ["🏠 Home", "🛕 Temple Explorer", "🚗 Travel Planner", "💰 Budget Planner", "🌸 My Yatra"], key="navigation")
search = st.sidebar.text_input("Search temples or places")
search_cols = [c for c in df.columns if any(k in c.lower() for k in ("peetha","temple","place","city","state","country","goddess"))]
if search:
    mask = pd.Series(False,index=df.index)
    for c in search_cols or [NAME]:
        mask |= df[c].astype(str).str.contains(search,case=False,regex=False,na=False)
    subset = df.loc[mask]
else:
    subset = df
if subset.empty:
    st.warning("No matching temples. Change the search text.")
    st.stop()
if ("selected_temple_index" in st.session_state
        and st.session_state["selected_temple_index"] not in subset.index):
    del st.session_state["selected_temple_index"]
index = st.sidebar.selectbox("Select Shakti Peetha", list(subset.index),
                             format_func=lambda i: str(df.loc[i,NAME]),
                             key="selected_temple_index")
row = df.loc[index]
temple = str(row[NAME])
place = value(row,"city")
state = value(row,"state")
country = value(row,"country")
destination = ", ".join(x for x in (temple,place,state,country) if x != "Not available")
st.sidebar.caption(f"Dataset: {csv_path.name}")
st.markdown('<div class="hero"><h1>🛕 Shakti Peetha Yatra</h1><p>Explore sacred destinations • Plan your journey from Hyderabad</p></div>',unsafe_allow_html=True)

if page == "🏠 Home":
    a,b,c = st.columns(3)
    a.metric("Sacred destinations",len(df))
    b.metric("Starting city","Hyderabad")
    c.metric("Selected destination",temple)
    st.subheader("🌺 Discover the Shakti Peethas")
    st.button("🛕 Discover Peethas — Open Temple Explorer",
              type="primary", use_container_width=True,
              on_click=open_temple)
    st.caption("Or choose any temple below and click Explore Temple to open it directly.")
    for start in range(0,len(subset),3):
        cards = st.columns(3)
        for card,(temple_idx,r) in zip(cards,subset.iloc[start:start+3].iterrows()):
            with card:
                with st.container(border=True):
                    st.markdown("### 🌸 " + str(r[NAME]))
                    st.write(value(r,"city"),"•",value(r,"state"))
                    st.button("🌸 Explore Temple", key=f"explore_{temple_idx}",
                              use_container_width=True,
                              on_click=open_temple, args=(temple_idx,))


elif page == "🛕 Temple Explorer":
    st.title("🌺 " + temple)
    details,photos,sights,hotels = st.tabs(["Details","Online Photos","Sightseeing","Hotels"])
    with details:
        fields(row,[""])
    with photos:
        key = next((term for term in IMAGE_TERMS if term in temple.lower()),None)
        query = IMAGE_TERMS[key] if key else destination
        st.caption("Wikimedia Commons search: " + query)
        st.warning("Search results are not verified temple photographs. Check each source before using it.")
        if st.button("Search online temple photos"):
            images = commons_images(query)
            if not images:
                st.info("No online photographs found for this search.")
            for start in range(0,min(len(images),6),3):
                columns = st.columns(3)
                for col,(url,title,source) in zip(columns,images[start:start+3]):
                    with col:
                        try:
                            st.image(url,caption=title,use_container_width=True)
                        except Exception:
                            st.caption("Image preview unavailable")
                        if source:
                            st.markdown(f"[View image source]({source})")
    with sights:
        fields(row,["sightseeing","tourist","attraction"])
        st.link_button("🗺️ Find nearby attractions",map_link("tourist attractions near " + destination))
    with hotels:
        fields(row,["hotel","accommodation","stay"])
        st.link_button("🏨 Find hotels on Google Maps",map_link("hotels near " + destination))
        st.caption("Confirm prices and availability with the property.")

elif page == "🚗 Travel Planner":
    st.title("🧭 Hyderabad to " + temple)
    a,b,c = st.columns(3)
    a.metric("Road distance",value(row,"road","distance"))
    b.metric("Nearest railway station",value(row,"railway","station"))
    c.metric("Destination airport",value(row,"destination","airport"))
    fields(row,["distance","highway","route","railway","airport","bus","travel","trip days","nights","transport"])
    directions = "https://www.google.com/maps/dir/?api=1&origin=" + quote("Hyderabad, Telangana, India") + "&destination=" + quote(destination)
    st.link_button("🗺️ Open Google Maps directions",directions)
    st.warning("Verify visa, border access and actual travel routes for international or restricted locations.")

elif page == "💰 Budget Planner":
    st.title("💰 Pilgrimage Cost Calculator")
    a,b,c = st.columns(3)
    with a: people = st.number_input("Travellers",min_value=1,max_value=30,value=2)
    with b: days = st.number_input("Trip days",min_value=1,max_value=30,value=2)
    with c: mode = st.selectbox("Travel mode",["Bus","Train","Car"])
    d,e = st.columns(2)
    with d: hotel_rate = st.number_input("Hotel room per night (₹)",min_value=0,value=1500,step=100)
    with e: food_rate = st.number_input("Food per person per day (₹)",min_value=0,value=500,step=50)
    distance = number_from_text(value(row,"road","distance"))
    if distance is None:
        st.warning("No numeric road distance in CSV for this temple.")
    else:
        transport = distance * 2 * ({"Bus":2.5,"Train":1.5,"Car":9}[mode]) * (1 if mode=="Car" else people)
        lodging = math.ceil(people/2) * max(days-1,0) * hotel_rate
        food = people * days * food_rate
        total = transport + lodging + food
        x,y,z = st.columns(3)
        x.metric("Transport",f"₹{transport:,.0f}")
        y.metric("Accommodation",f"₹{lodging:,.0f}")
        z.metric("Food",f"₹{food:,.0f}")
        st.success(f"Estimated total: ₹{total:,.0f}")
        st.bar_chart(pd.DataFrame({"Cost (₹)": [transport,lodging,food]},index=["Transport","Hotel","Food"]))
        st.caption("Illustrative estimates only. Train/bus calculations use road distance as a proxy. Actual fares, routes, visas and permits may differ.")

elif page == "🌸 My Yatra":
    st.title("🌸 My Pilgrimage Checklist")
    names = df[NAME].astype(str).tolist()
    visited = st.multiselect("Temples visited",names,key="visited_temples")
    st.metric("Completed",f"{len(visited)} / {len(names)}")
    st.progress(len(visited)/len(names))
    st.subheader("Remaining destinations")
    for name in names:
        if name not in visited:
            st.write("☐",name)
    st.caption("Checklist is stored in the current Streamlit session only.")

st.divider()
st.caption("Shakti Peetha Yatra • Local Streamlit application • Source: your CSV dataset")
