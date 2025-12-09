from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Staff, Leave
from .forms import StaffForm, LeaveForm


# ==================== STAFF VIEWS ====================

@login_required
def staff_list(request):
    """List all staff members"""
    staff = Staff.objects.all().select_related('user', 'department', 'designation').order_by('-created_at')
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        staff = staff.filter(
            user__first_name__icontains=search_query
        ) | staff.filter(
            user__last_name__icontains=search_query
        ) | staff.filter(
            employee_id__icontains=search_query
        )
    
    paginator = Paginator(staff, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'school/staff/list.html', {
        'staff': page_obj,
        'search_query': search_query
    })


@login_required
def staff_create(request):
    """Create new staff member"""
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            staff = form.save()
            messages.success(request, f'Staff member {staff.user.get_full_name()} added successfully!')
            return redirect('staff:staff_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StaffForm()
    
    return render(request, 'school/staff/staff_form.html', {
        'form': form
    })


@login_required
def staff_edit(request, pk):
    """Edit existing staff member"""
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, f'Staff member {staff.user.get_full_name()} updated successfully!')
            return redirect('staff:staff_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StaffForm(instance=staff)
    
    return render(request, 'school/staff/staff_form.html', {
        'form': form
    })


@login_required
def staff_delete(request, pk):
    """Delete staff member"""
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        name = staff.user.get_full_name()
        staff.delete()
        messages.success(request, f'Staff member {name} deleted successfully!')
        return redirect('staff:staff_list')
    
    return render(request, 'school/staff/staff_confirm_delete.html', {
        'staff': staff
    })


@login_required
def staff_detail(request, pk):
    """View staff member details"""
    staff = get_object_or_404(Staff, pk=pk)
    return render(request, 'school/staff/detail.html', {
        'staff': staff
    })


# ==================== LEAVE VIEWS ====================

@login_required
def leave_list(request):
    """List all leave applications"""
    leaves = Leave.objects.all().select_related('staff').order_by('-start_date')
    return render(request, 'school/staff/leave_list.html', {
        'leaves': leaves
    })


@login_required
def leave_create(request):
    """Create new leave application"""
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save()
            messages.success(request, 'Leave application submitted successfully!')
            return redirect('staff:leave_list')
    else:
        form = LeaveForm()
    
    return render(request, 'school/staff/leave_form.html', {
        'form': form
    })


@login_required
def leave_edit(request, pk):
    """Edit leave application"""
    leave = get_object_or_404(Leave, pk=pk)
    if request.method == 'POST':
        form = LeaveForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            messages.success(request, 'Leave application updated successfully!')
            return redirect('staff:leave_list')
    else:
        form = LeaveForm(instance=leave)
    
    return render(request, 'school/staff/leave_form.html', {
        'form': form
    })


@login_required
def leave_approve(request, pk):
    """Approve/Reject leave application"""
    leave = get_object_or_404(Leave, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['APPROVED', 'REJECTED']:
            leave.status = status
            leave.save()
            messages.success(request, f'Leave application {status.lower()} successfully!')
        return redirect('staff:leave_list')
    
    return render(request, 'school/staff/leave_approve.html', {
        'leave': leave
    })
