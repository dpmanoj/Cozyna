from django.conf.urls import url, include
from .views import index, sitCounter, entered
import views
# from .views import
urlpatterns = [
    url(r'^sit/', sitCounter.as_view()),
    url(r'^entered/', entered.as_view()),
    url(r'^table/1/startsit/', views.table_one_startSit.as_view()),
    url(r'^table/2/startsit/', views.table_two_startSit.as_view()),
    url(r'^table/3/startsit/', views.table_three_startSit.as_view()),
    url(r'^table/4/startsit/', views.table_four_startSit.as_view()),
    url(r'^table/5/startsit/', views.table_five_startSit.as_view()),
    url(r'^table/6/startsit/', views.table_six_startSit.as_view()),
    url(r'^table/7/startsit/', views.table_seven_startSit.as_view()),
    url(r'^table/8/startsit/', views.table_eight_startSit.as_view()),
    url(r'^table/9/startsit/', views.table_nine_startSit.as_view()),
    url(r'^table/10/startsit/', views.table_ten_startSit.as_view()),
    url(r'^table/11/startsit/', views.table_eleven_startSit.as_view()),
    url(r'^table/12/startsit/', views.table_twelve_startSit.as_view()),
    url(r'^table/13/startsit/', views.table_thirteen_startSit.as_view()),
    url(r'^table/14/startsit/', views.table_fourteen_startSit.as_view()),
    url(r'^table/15/startsit/', views.table_fifteen_startSit.as_view()),
    url(r'^table/16/startsit/', views.table_sixteen_startSit.as_view()),
    url(r'^table/17/startsit/', views.table_seventeen_startSit.as_view()),
    url(r'^table/18/startsit/', views.table_eighteen_startSit.as_view()),
    url(r'^table/19/startsit/', views.table_nineteen_startSit.as_view()),
    url(r'^table/20/startsit/', views.table_twenty_startSit.as_view()),

    url(r'^table/1/ordered/', views.table_one_ordered.as_view()),
    url(r'^table/2/ordered/', views.table_two_ordered.as_view()),
    url(r'^table/3/ordered/', views.table_three_ordered.as_view()),
    url(r'^table/4/ordered/', views.table_four_ordered.as_view()),
    url(r'^table/5/ordered/', views.table_five_ordered.as_view()),
    url(r'^table/6/ordered/', views.table_six_ordered.as_view()),
    url(r'^table/7/ordered/', views.table_seven_ordered.as_view()),
    url(r'^table/8/ordered/', views.table_eight_ordered.as_view()),
    url(r'^table/9/ordered/', views.table_nine_ordered.as_view()),
    url(r'^table/10/ordered/', views.table_ten_ordered.as_view()),
    url(r'^table/11/ordered/', views.table_eleven_ordered.as_view()),
    url(r'^table/12/ordered/', views.table_twelve_ordered.as_view()),
    url(r'^table/13/ordered/', views.table_thirteen_ordered.as_view()),
    url(r'^table/14/ordered/', views.table_fourteen_ordered.as_view()),
    url(r'^table/15/ordered/', views.table_fifteen_ordered.as_view()),
    url(r'^table/16/ordered/', views.table_sixteen_ordered.as_view()),
    url(r'^table/17/ordered/', views.table_seventeen_ordered.as_view()),
    url(r'^table/18/ordered/', views.table_eighteen_ordered.as_view()),
    url(r'^table/19/ordered/', views.table_nineteen_ordered.as_view()),
    url(r'^table/20/ordered/', views.table_twenty_ordered.as_view()),

    url(r'^table/1/arrived/', views.table_one_arrived.as_view()),
    url(r'^table/2/arrived/', views.table_two_arrived.as_view()),
    url(r'^table/3/arrived/', views.table_three_arrived.as_view()),
    url(r'^table/4/arrived/', views.table_four_arrived.as_view()),
    url(r'^table/5/arrived/', views.table_five_arrived.as_view()),
    url(r'^table/6/arrived/', views.table_six_arrived.as_view()),
    url(r'^table/7/arrived/', views.table_seven_arrived.as_view()),
    url(r'^table/8/arrived/', views.table_eight_arrived.as_view()),
    url(r'^table/9/arrived/', views.table_nine_arrived.as_view()),
    url(r'^table/10/arrived/', views.table_ten_arrived.as_view()),
    url(r'^table/11/arrived/', views.table_eleven_arrived.as_view()),
    url(r'^table/12/arrived/', views.table_twelve_arrived.as_view()),
    url(r'^table/13/arrived/', views.table_thirteen_arrived.as_view()),
    url(r'^table/14/arrived/', views.table_fourteen_arrived.as_view()),
    url(r'^table/15/arrived/', views.table_fifteen_arrived.as_view()),
    url(r'^table/16/arrived/', views.table_sixteen_arrived.as_view()),
    url(r'^table/17/arrived/', views.table_seventeen_arrived.as_view()),
    url(r'^table/18/arrived/', views.table_eighteen_arrived.as_view()),
    url(r'^table/19/arrived/', views.table_nineteen_arrived.as_view()),
    url(r'^table/20/arrived/', views.table_twenty_arrived.as_view()),

    url(r'^table/1/finished/', views.table_one_finished.as_view()),
    url(r'^table/2/finished/', views.table_two_finished.as_view()),
    url(r'^table/3/finished/', views.table_three_finished.as_view()),
    url(r'^table/4/finished/', views.table_four_finished.as_view()),
    url(r'^table/5/finished/', views.table_five_finished.as_view()),
    url(r'^table/6/finished/', views.table_six_finished.as_view()),
    url(r'^table/7/finished/', views.table_seven_finished.as_view()),
    url(r'^table/8/finished/', views.table_eight_finished.as_view()),
    url(r'^table/9/finished/', views.table_nine_finished.as_view()),
    url(r'^table/10/finished/', views.table_ten_finished.as_view()),
    url(r'^table/11/finished/', views.table_eleven_finished.as_view()),
    url(r'^table/12/finished/', views.table_twelve_finished.as_view()),
    url(r'^table/13/finished/', views.table_thirteen_finished.as_view()),
    url(r'^table/14/finished/', views.table_fourteen_finished.as_view()),
    url(r'^table/15/finished/', views.table_fifteen_finished.as_view()),
    url(r'^table/16/finished/', views.table_sixteen_finished.as_view()),
    url(r'^table/17/finished/', views.table_seventeen_finished.as_view()),
    url(r'^table/18/finished/', views.table_eighteen_finished.as_view()),
    url(r'^table/19/finished/', views.table_nineteen_finished.as_view()),
    url(r'^table/20/finished/', views.table_twenty_finished.as_view()),

    url(r'^table/1/endSit/', views.table_one_endSit.as_view()),
    url(r'^table/2/endSit/', views.table_two_endSit.as_view()),
    url(r'^table/3/endSit/', views.table_three_endSit.as_view()),
    url(r'^table/4/endSit/', views.table_four_endSit.as_view()),
    url(r'^table/5/endSit/', views.table_five_endSit.as_view()),
    url(r'^table/6/endSit/', views.table_six_endSit.as_view()),
    url(r'^table/7/endSit/', views.table_seven_endSit.as_view()),
    url(r'^table/8/endSit/', views.table_eight_endSit.as_view()),
    url(r'^table/9/endSit/', views.table_nine_endSit.as_view()),
    url(r'^table/10/endSit/', views.table_ten_endSit.as_view()),
    url(r'^table/11/endSit/', views.table_eleven_endSit.as_view()),
    url(r'^table/12/endSit/', views.table_twelve_endSit.as_view()),
    url(r'^table/13/endSit/', views.table_thirteen_endSit.as_view()),
    url(r'^table/14/endSit/', views.table_fourteen_endSit.as_view()),
    url(r'^table/15/endSit/', views.table_fifteen_endSit.as_view()),
    url(r'^table/16/endSit/', views.table_sixteen_endSit.as_view()),
    url(r'^table/17/endSit/', views.table_seventeen_endSit.as_view()),
    url(r'^table/18/endSit/', views.table_eighteen_endSit.as_view()),
    url(r'^table/19/endSit/', views.table_nineteen_endSit.as_view()),
    url(r'^table/20/endSit/', views.table_twenty_endSit.as_view()),
]
