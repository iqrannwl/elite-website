def breadcrumbs(request):
    path = request.path.strip("/").split("/")  # Get URL parts
    breadcrumbs = [{"name": "Home", "url": "/"}]  # Always start with Home

    url_accumulator = ""
    for part in path:
        url_accumulator += f"/{part}"
        name = part.replace("-", " ").title()  # Convert "blog-post" → "Blog Post"
        breadcrumbs.append({"name": name, "url": url_accumulator})

    return {"breadcrumbs": breadcrumbs}
