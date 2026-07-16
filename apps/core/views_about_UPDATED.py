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

    # ── "What We Distribute" — every product, grouped by category ──
    # Pulls real Product rows (real name + real display_image) instead of
    # a hardcoded list, so this section always matches what's actually in
    # the catalogue/admin — add a product in the admin and it shows up
    # here automatically, with whatever photo is attached to it.
    categories_meta = [
        ('pesticide',  'bug',        'Pesticides',
         "Fast, reliable knockdown for the insects that eat into your harvest — from aphids and bollworm to stem borers."),
        ('herbicide',  'seedling',   'Herbicides',
         "Clear stubborn weeds like Couch and Kikuyu grass without setting your crop back — selective and non-selective options."),
        ('fungicide',  'microscope', 'Fungicides',
         "Protective and curative cover against blight, mildew and rot — built for Uganda's humidity and rainfall patterns."),
        ('other',      'boxes',      'Fertilizers & Equipment',
         "Balanced nutrition and the spraying equipment to apply it right — from basal fertilizer to a dependable knapsack sprayer."),
    ]
    product_groups = []
    for cat, icon, title, blurb in categories_meta:
        products = Product.objects.filter(category=cat)
        if products.exists():
            product_groups.append({'icon': icon, 'title': title, 'blurb': blurb, 'products': products})

    return render(request,'about.html',{'stats_list':stats_list,'faqs':faqs,'product_groups':product_groups})
