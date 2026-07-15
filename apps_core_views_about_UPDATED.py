def about(request):
    stats_list=[('2020','Year Founded'),(f'{Product.objects.count()}+','Product Lines'),
                (f'{Distributor.objects.count()}+','Distributor Outlets'),('4','Regions Covered')]
    faqs=[
        ('Are your products MAAIF-registered?','Yes. All products distributed by MACL are registered with Uganda\'s Ministry of Agriculture, Animal Industry and Fisheries (MAAIF). Certificates available on request.'),
        ('Do you sell wholesale?','Absolutely. We supply retail and wholesale. Contact us at +256 772 507582 for bulk pricing and distributor partnerships.'),
        ('How do I choose the right product?','Call us or visit our Kampala office. Describe your crop and pest/weed/disease — our team will recommend the right product, dosage and timing.'),
        ('Are your products environmentally safe?','All registered products include environmental safety assessments. Follow label instructions: buffer zones, pre-harvest intervals, and proper PPE.'),
        ('Do you deliver upcountry?','Products available through our 11-outlet nationwide network. Use our Store Locator. For large bulk orders, direct delivery can be arranged.'),
        ('What is the minimum order?','No minimum for retail. For wholesale, minimums vary by product — contact our sales team.'),
        ('How do I report a product problem?','Call +256 772 507582 or email kulanju_w@yahoo.com. Keep the product, note the batch number, and describe the issue. We investigate all complaints.'),
        ('What is your return policy?','Sealed, unused products in original packaging may be returned within 7 days with proof of purchase.'),
    ]

    # ── "What We Distribute" — grouped by category, KOIX icon-card style ──
    # Replaces the old flat 18-box grid with warmer, human copy per category.
    product_groups = [
        {
            'icon': 'bug', 'title': 'Pesticides',
            'blurb': "Fast, reliable knockdown for the insects that eat into your harvest — from aphids and bollworm to stem borers.",
            'items': ['MD Acelemectin 48EC', 'MD FOS 48EC', 'Top Fenos 50EC', 'MD Thion 350EC', 'MD Thoate 40EC'],
        },
        {
            'icon': 'seedling', 'title': 'Herbicides',
            'blurb': "Clear stubborn weeds like Couch and Kikuyu grass without setting your crop back — selective and non-selective options.",
            'items': ['Muddosate 480SL', 'MD Maize Plus 40OD', 'Max 2,4-D 720SL', 'MD Ametryn 500SC', 'Weed IT 75.7 XL'],
        },
        {
            'icon': 'microscope', 'title': 'Fungicides',
            'blurb': "Protective and curative cover against blight, mildew and rot — built for Uganda's humidity and rainfall patterns.",
            'items': ['Top-Laxly M 72WP', 'MD Top Laxlyn 72WP', 'Toplaxly 72WP', 'Copper Oxychloride 850WP'],
        },
        {
            'icon': 'boxes', 'title': 'Fertilizers & Equipment',
            'blurb': "Balanced nutrition and the spraying equipment to apply it right — from basal fertilizer to a dependable knapsack sprayer.",
            'items': ['Urea 46%N', 'NPK 17:17:17', 'Foliar Boost 20-20-20+TE', 'Knapsack Sprayer 16L'],
        },
    ]

    return render(request,'about.html',{'stats_list':stats_list,'faqs':faqs,'product_groups':product_groups})
