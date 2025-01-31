from django.shortcuts import render, redirect
from django.contrib import messages
from adminUser.models import Category  # Ensure that you import your Category model



def addCounseling(request):
    return render(request, 'admin/counseling/addCounseling.html')


def viewCounseling(request):
    return render(request, 'admin/counseling/addCounseling.html')
    


# View for adding category
def addCategory(request):
    if request.method == 'POST':
        # Retrieve category and description from POST data
        category_name = request.POST.get('category')  # Match the field name 'category'
        description = request.POST.get('description')

        # Ensure both fields are filled
        if category_name and description:
            # Create a new Category instance and save it
            new_category = Category(category=category_name, description=description)
            new_category.save()

            # Add a success message and redirect to the same page
            messages.success(request, 'Category has been added successfully.')
            return redirect('addCategory')  # Redirect to the category list or same page
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'admin/counseling/add-category.html')