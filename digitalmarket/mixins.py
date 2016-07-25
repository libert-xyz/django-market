from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kargs)


class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kargs)
