from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),

    path('administration/', views.administration, name='administration'),
    path('add_time/', views.add_time, name='add_time'),
    path('submit_time/', views.submit_time, name='submit_time'),
    path('inactivate_account/', views.inactivate_account, name='inactivate_account'),
    path('activate_account/', views.activate_account, name='activate_account'),

    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('payment/', views.payment, name='payment'),
    path('contact/', views.contact, name='contact'),
    path('set_customer_as_paid/', views.set_customer_as_paid, name='set_customer_as_paid'),

    path('start/', views.start, name='start'),
    path('inspiration/', views.inspiration, name='inspiration'),
    path('tools/', views.tools, name='tools'),
    path('future/', views.future, name='future'),

    path('benefits/', views.benefits, name='benefits'),
    path('grid/', views.grid, name='grid'),
    path('separation/', views.separation, name='separation'),
    path('visual_noise/', views.visual_noise, name='visual_noise'),
    path('balance/', views.balance, name='balance'),
    path('iconography/', views.iconography, name='iconography'),
    path('typography_fundation/', views.typography_fundation, name='typography_fundation'),
    path('typography_scale/', views.typography_scale, name='typography_scale'),
    path('color_contrast/', views.color_contrast, name='color-contrast'),
    path('color_palette/', views.color_palette, name='color_palette'),
    path('spacing/', views.spacing, name='spacing'),
    path('composition/', views.composition, name='composition'),
    path('consistency/', views.consistency, name='consistency'),
    path('resources/', views.resources, name='resources'),

    path('layers/', views.layers, name='layers'),
    path('history_tool/', views.history_tool, name='history_tool'),
    path('zoom_tool/', views.zoom_tool, name='zoom_tool'),
    path('rectangle_tool/', views.rectangle_tool, name='rectangle_tool'),
    path('elipse_tool/', views.elipse_tool, name='elipse_tool'),
    path('line_tool/', views.line_tool, name='line_tool'),
    path('color/', views.color, name='color'),
    path('gradient/', views.gradient, name='gradient'),
    path('drop_shadow/', views.drop_shadow, name='drop_shadow'),
    path('transparency/', views.transparency, name='transparency'),
    path('masking/', views.masking, name='masking'),
    path('text_tool/', views.text_tool, name='text_tool'),
    path('font_icons/', views.font_icons, name='font_icons'),

    path('text_fields/', views.text_fields, name='text_fields'),
    path('buttons/', views.buttons, name='buttons'),
    path('sliders/', views.sliders, name='sliders'),
    path('selection_controls/', views.selection_controls, name='selection_controls'),
    path('chips/', views.chips, name='chips'),
    path('tooltips/', views.tooltips, name='tooltips'),
    path('cards/', views.cards, name='cards'),
    path('dialogs/', views.dialogs, name='dialogs'),
    path('lists/', views.lists, name='lists'),
    path('tables/', views.tables, name='tables'),
    path('navigations/', views.navigations, name='navigations'),
    path('charts/', views.charts, name='charts'),
    path('menus/', views.menus, name='menus'),
    path('steps/', views.steps, name='steps'),
    path('snackbars/', views.snackbars, name='snackbars'),

    path('registration_interface/', views.registration_interface, name='registration_interface'),
    path('application_interface/', views.application_interface, name='application_interface'),
    path('user_flows/', views.user_flows, name='user_flows'),
    path('interactive_prototype/', views.interactive_prototype, name='interactive_prototype'),

    path('sample_app_instagram/', views.sample_app_instagram, name='sample_app_instagram'),
    path('sample_app_facebook/', views.sample_app_facebook, name='sample_app_facebook'),
    path('iterations/', views.iterations, name='iterations'),

    path('rlp_spec/', views.spec, name='spec'),
    path('rlp_wireframes/', views.wireframes, name='wireframes'),
    path('rlp_user_flows/', views.rlp_user_flows, name='rlp_user_flows'),
    path('rlp_prototype/', views.prototype, name='prototype'),
    path('rlp_design/', views.design, name='design'),
    path('rlp_design_guide/', views.design_guide, name='design_guide'),
    path('rlp_assets/', views.assets, name='assets'),

    path('portfolio/', views.portfolio, name='portfolio'),
    path('client/', views.client, name='client'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
