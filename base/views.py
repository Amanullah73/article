from django.shortcuts import render

# Create your views here.
article_data = [
    {
        "id": 1,
        "title": "All About QSpiders",
        "desc": "QSpiders is a popular software training institute that provides courses in Python, Java, Testing, SQL, Django, and Full Stack Development with placement assistance.",
        "image": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"
    },

    {
        "id": 2,
        "title": "All About Goa",
        "desc": "Goa is one of India’s most famous tourist destinations, known for its beautiful beaches, nightlife, seafood, Portuguese culture, and relaxing atmosphere.",
        "image": "https://images.unsplash.com/photo-1518509562904-e7ef99cdcc86"
    },

    {
        "id": 3,
        "title": "All About Thailand",
        "desc": "Thailand is a Southeast Asian country famous for tropical beaches, temples, floating markets, delicious street food, and vibrant city life.",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
    },

    {
        "id": 4,
        "title": "All About Bangalore",
        "desc": "Bangalore, officially Bengaluru, is known as the Silicon Valley of India and is famous for IT companies, pleasant weather, cafes, and startup culture.",
        "image": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2"
    },

    {
        "id": 5,
        "title": "All About Basavanagudi",
        "desc": "Basavanagudi is one of Bangalore’s oldest and most culturally rich areas, known for temples, food streets, traditional markets, and heritage buildings.",
        "image": "https://images.unsplash.com/photo-1587474260584-136574528ed5"
    },

    {
        "id": 6,
        "title": "All About Mysore",
        "desc": "Mysore is famous for its royal heritage, Mysore Palace, Dasara festival, sandalwood products, and rich cultural traditions.",
        "image": "https://images.unsplash.com/photo-1605640840605-14ac1855827b"
    },

    {
        "id": 7,
        "title": "All About Kerala",
        "desc": "Kerala is known for its backwaters, houseboats, green landscapes, ayurvedic treatments, and beautiful hill stations.",
        "image": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944"
    },

    {
        "id": 8,
        "title": "All About Dubai",
        "desc": "Dubai is a modern city in the UAE famous for luxury shopping, skyscrapers, desert safaris, and world-class attractions.",
        "image": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c"
    },

    {
        "id": 9,
        "title": "All About Paris",
        "desc": "Paris, the capital of France, is known for the Eiffel Tower, fashion, art museums, romantic atmosphere, and historic architecture.",
        "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34"
    },

    {
        "id": 10,
        "title": "All About Maldives",
        "desc": "The Maldives is famous for crystal-clear water, luxury resorts, water villas, coral reefs, and peaceful island experiences.",
        "image": "https://images.unsplash.com/photo-1573843981267-be1999ff37cd"
    }
]
def home(request):
    return render(request,'home.html',{'data':article_data})

def read(request,pk):
    print(pk)
    for i in article_data:
        if i['id'] == pk:
            context = {'data':i}
    return render(request,'read.html',context)


news_data = [
    {
        "id": 1,
        "title": "India Launches New Space Mission",
        "desc": "ISRO successfully launched a new satellite mission aimed at improving weather forecasting and communication systems.",
        "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa"
    },

    {
        "id": 2,
        "title": "Bangalore Startup Raises Funding",
        "desc": "A Bengaluru-based AI startup secured major international funding to expand its innovative technology solutions.",
        "image": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3"
    },

    {
        "id": 3,
        "title": "Heavy Rain Expected in Kerala",
        "desc": "The weather department has issued alerts for heavy rainfall across several districts in Kerala this week.",
        "image": "https://images.unsplash.com/photo-1500375592092-40eb2168fd21"
    },

    {
        "id": 4,
        "title": "New Electric Cars Introduced",
        "desc": "Several automobile companies introduced affordable electric vehicles with advanced battery technology.",
        "image": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7"
    },

    {
        "id": 5,
        "title": "Tourism Increases in Goa",
        "desc": "Goa witnessed a huge increase in tourist arrivals during the holiday season, boosting local businesses.",
        "image": "https://images.unsplash.com/photo-1518509562904-e7ef99cdcc86"
    }
]

# News Home Page
def news_home(request):
    return render(request, 'news_home.html', {'data': news_data})


# News Detail Page
def news_read(request, pk):
    for i in news_data:
        if i['id'] == pk:
            context = {'data': i}
            return render(request, 'news_read.html', context)
        


event_data = [

    {
        "id": 1,
        "title": "Tech Conference 2026",
        "desc": "Join the biggest technology conference with top speakers, AI workshops, startup networking, and innovation showcases.",
        "image": "https://images.unsplash.com/photo-1511578314322-379afb476865"
    },

    {
        "id": 2,
        "title": "Music Fest Bangalore",
        "desc": "Experience live music performances from famous bands, DJs, and artists at Bangalore’s biggest music festival.",
        "image": "https://images.unsplash.com/photo-1501386761578-eac5c94b800a"
    },

    {
        "id": 3,
        "title": "Food Carnival",
        "desc": "Enjoy delicious street food, desserts, traditional dishes, and international cuisines at the grand food carnival.",
        "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836"
    },

    {
        "id": 4,
        "title": "Startup Meetup",
        "desc": "Connect with entrepreneurs, investors, and developers to discuss startup ideas and business opportunities.",
        "image": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"
    },

    {
        "id": 5,
        "title": "Art & Culture Expo",
        "desc": "Explore paintings, handicrafts, dance performances, and cultural exhibitions from talented artists.",
        "image": "https://images.unsplash.com/photo-1460661419201-fd4cecdf8a8b"
    }

]

# ================= EVENTS HOME PAGE =================

def event_home(request):
    return render(request, 'event_home.html', {'data': event_data})


# ================= EVENT DETAIL PAGE =================

def event_read(request, pk):

    for i in event_data:

        if i['id'] == pk:

            context = {'data': i}

            return render(request, 'event_read.html', context)
        
sports_data = [

    {
        "id": 1,
        "title": "RCB Playoffs Charge 2026",
        "desc": "Royal Challengers Bengaluru have officially qualified for the IPL 2026 playoffs and are looking dominant this season with Virat Kohli leading from the front.",
        "image": "https://images.unsplash.com/photo-1540747913346-19e32dc3e97e"
    },

    {
        "id": 2,
        "title": "IPL 2026 Fever",
        "desc": "IPL 2026 is trending worldwide with packed stadiums, dramatic finishes, and top franchises battling for playoff glory.",
        "image": "https://images.unsplash.com/photo-1574629810360-7efbbe195018"
    },

    {
        "id": 3,
        "title": "Virat Kohli Dominance",
        "desc": "Virat Kohli continues to shine in IPL 2026 with match-winning performances, record-breaking runs, and iconic celebrations for RCB.",
        "image": "https://images.unsplash.com/photo-1517649763962-0c623066013b"
    },

    {
        "id": 4,
        "title": "Chinnaswamy Stadium Energy",
        "desc": "The electrifying atmosphere at Bengaluru’s Chinnaswamy Stadium has become one of the biggest highlights of IPL 2026.",
        "image": "https://images.unsplash.com/photo-1508098682722-e99c643e7485"
    },

    {
        "id": 5,
        "title": "RCB Fan Army 2026",
        "desc": "The passionate RCB fanbase continues to trend across social media with massive support, viral chants, and unforgettable match-day moments.",
        "image": "https://images.unsplash.com/photo-1560272564-c83b66b1ad12"
    }

]
# ================= SPORTS HOME PAGE =================

def sports_home(request):

    return render(request, 'sports_home.html', {'data': sports_data})


# ================= SPORTS READ PAGE =================

def sports_read(request, pk):

    for i in sports_data:

        if i['id'] == pk:

            context = {'data': i}

            return render(request, 'sports_read.html', context)