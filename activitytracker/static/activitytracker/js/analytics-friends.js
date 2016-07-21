/**
 * Created by Aggelos.
 */

    var svg = dimple.newSvg(".analytics-topChart", "100%", 650);
    var svg2 = dimple.newSvg(".analytics-bottomChart", "100%", 650);

    $('select[name="friend-select"], #dateRange, select[name="activity-select"], #allActivitiesChecked, #allFriendsChecked').on('change', function(){
        if ($("#allFriendsChecked").prop('checked')) {

            $('#friend-select').prop('disabled', true).trigger("chosen:updated");
            if ($("#allActivitiesChecked").prop('checked')) {
                //$('#metric-select').prop('disabled', false);
                //$('#activity-select').prop('disabled', true).trigger("chosen:updated");
                AllActivitiesAllFriends();
                updateFriendsBanner('all','all');
            }
            else {
                $('#metric-select').prop('disabled', false);
                $('#activity-select').prop('disabled', false).trigger("chosen:updated");
                OneActivityAllFriends();
                updateFriendsBanner($('#activity-select').val(), 'all')
            }
        }
        else {
            $('#metric-select').prop('disabled', false);
            $('#friend-select').prop('disabled', false).trigger("chosen:updated");
            if ($("#allActivitiesChecked").prop('checked')) {
                $('#activity-select').prop('disabled', true).trigger("chosen:updated");
                OneFriendAllActivities();
                updateFriendsBanner('all', $('#friend-select').val())
            }
            else {
                $('#metric-select').prop('disabled', true);
				$('#activity-select').prop('disabled', false).trigger("chosen:updated");
                OneActivityOneFriend();
                updateFriendsBanner($('#activity-select').val(), $('#friend-select').val())
            }
        }
    });

    function OneFriendAllActivities() {
    	var friend_chosen = $('#friend-select').val();
        var range = $('#dateRange').val();
        var metric = $('#metric-select').val();
        $('.analytics-topChart h1').text('Category/Activity Distribution');
        $('.analytics-bottomChart h1').text('Timeorder Activity Analysis');
		$.ajax({
			type: "post",
			data: {friend: friend_chosen, csrfmiddlewaretoken: getCookie('csrftoken'), range: range},
			cache: false,
			url: BASE_URL + 'analytics/friends/update/activities_friend/',
			dataType: "json",
			error: function (xhr, status, error) {
				Done();
				console.log('went bad');
			},
			success: function (response) {
                try {
                    svg.selectAll('*').remove();
                    svg2.selectAll('*').remove();
                }
                catch(err) {}
                var chartOuter = new dimple.chart(svg, response[1]);
                var chartInner = new dimple.chart(svg, response[0]);
                chartOuter.setBounds('5%', '10%', '75%', '80%');
                chartInner.setBounds('5%', '10%', '75%', '80%');

                var inner_p, outer_p;
                if ( metric == "Number of Instances") {
                    outer_p = chartOuter.addMeasureAxis("p", "Instances");
                    inner_p = chartInner.addMeasureAxis("p", "Instances");
				}
                else{
                    outer_p = chartOuter.addMeasureAxis("p", "Hours");
                    inner_p = chartInner.addMeasureAxis("p", "Hours");
                }
				chartOuterLegend = chartOuter.addLegend("83%", 120, 90, 300, "left");
				chartInnerLegend = chartInner.addLegend("83%", 20, 90, 300, "left");
                var outerRing = chartOuter.addSeries("Activity", dimple.plot.pie);
                var innerRing = chartInner.addSeries("Category", dimple.plot.pie);
                outerRing.addOrderRule("Category");
                innerRing.addOrderRule("Category");
				outerRing.innerRadius = "-30px";
				innerRing.outerRadius = "-40px";
				innerRing.innerRadius = "-70px";

				chartOuter.defaultColors = [new dimple.color("#98abc5"), new dimple.color("#8a89a6"), new dimple.color("#ff8c00"),new dimple.color("#995411"),
                                            new dimple.color("#7b6888"), new dimple.color("#E07C27"), new dimple.color("#a05d56"), new dimple.color("#d0743c"),
                                            new dimple.color("#7b6888"), new dimple.color("#266419"), new dimple.color("#DF7821"), new dimple.color("#4DA4DA"),
                                            new dimple.color("#A5C59E"), new dimple.color("#5C5596"), new dimple.color("#CA9A9A"), new dimple.color("#D8E4EA"),
                                            new dimple.color("#326277"), new dimple.color("#9174A5"), new dimple.color("#7B0404"), new dimple.color("#EAE2EF"),
                                            new dimple.color("#562323"), new dimple.color("#03671F"), new dimple.color("#7b6888"), new dimple.color("#E3F25E"),
                                            new dimple.color("#F498DA"), new dimple.color("#6b486b") ];

                var orange_colors = ["rgb(182, 102, 54)","rgb(186, 87, 28)",
                                "rgb(202, 85, 16)","rgb(236, 98, 17)","rgb(253, 101, 12)","rgb(253, 128, 54)","rgb(252, 143, 52)",
                                "rgb(252, 181, 73)","rgb(252, 217, 143)","rgb(240, 168, 13)","rgb(253, 175, 7)","rgb(247, 202, 104)",
                                "rgb(224, 136, 18)","rgb(247, 232, 154)","rgb(247, 187, 108)","rgb(240, 209, 161)"];
                var blue_colors = ["rgb(6, 67, 86)","rgb(15, 88, 184)","rgb(11, 105, 132)","rgb(71, 122, 190)","rgb(37, 134, 163)","rgb(50, 158, 190)",
                                   "rgb(58, 180, 216)","rgb(64, 198, 237)","rgb(102, 215, 249)","rgb(140, 223, 247)","rgb(176, 235, 252)" ];

                var purple_colors = ["rgb(48, 17, 87)","rgb(88, 35, 115)","rgb(121, 28, 136)","rgb(129, 58, 140)","rgb(160, 78, 173)","rgb(183, 39, 207)",
                                   "rgb(224, 63, 250)","rgb(232, 111, 252)","rgb(239, 153, 253)","rgb(242, 192, 250)" ];

                var green_colors = ["rgb(40, 60, 6)","rgb(58, 84, 13)","rgb(82, 118, 20)","rgb(91, 144, 1)","rgb(101, 144, 29)","rgb(124, 179, 30)",
                                   "rgb(155, 219, 42)","rgb(170, 219, 84)","rgb(189, 240, 100)","rgb(102, 215, 249)","rgb(201, 249, 119)","rgb(217, 250, 159)" ];

                var red_colors = ["rgb(77, 7, 7)","rgb(95, 9, 9)","rgb(111, 0, 0)","rgb(145, 12, 12)","rgb(174, 2, 2)","rgb(194, 12, 12)",
                                   "rgb(221, 23, 23)","rgb(249, 13, 13)","rgb(253, 35, 35)","rgb(252, 63, 63)","rgb(247, 104, 104)","rgb(247, 162, 162)" ];

                var black_colors = ["rgb(8, 7, 7)","rgb(39, 33, 33)","rgb(63, 54, 54)","rgb(81, 74, 74)","rgb(94, 88, 88)","rgb(113, 108, 108)",
                                   "rgb(142, 139, 139)","rgb(169, 166, 166)","rgb(194, 189, 189)","rgb(252, 63, 63)","rgb(216, 213, 213)","rgb(239, 234, 234)" ];

                var color_dict = {"Communication/Socializing": blue_colors,
                              "Fun/Leisure/Hobbies": orange_colors,
                              "Responsibilities": red_colors,
                              "Self-care/Everyday Needs": black_colors,
                              "Transportation": purple_colors,
                              "Sports/Fitness": green_colors
                };
                var prev_category = "";
                var counter = 0;
                $.each(response[0], function(i, e) {
                    chartInner.assignColor(e.Category, e.Color);
                });
                $.each(response[1], function(i, e) {
                    if (e.Category != prev_category){
                        counter = 0
                    }
                    chartOuter.assignColor(e.Activity, color_dict[e.Category][counter%16]);
                    prev_category = e.Category;
                    counter += 1;
                });

				var barChart = new dimple.chart(svg2, response[1]);
                barChart.defaultColors = [new dimple.color("#98abc5"), new dimple.color("#8a89a6"), new dimple.color("#ff8c00"),new dimple.color("#995411"),
                                            new dimple.color("#7b6888"), new dimple.color("#E07C27"), new dimple.color("#a05d56"), new dimple.color("#d0743c"),
                                            new dimple.color("#7b6888"), new dimple.color("#266419"), new dimple.color("#DF7821"), new dimple.color("#4DA4DA"),
                                            new dimple.color("#A5C59E"), new dimple.color("#5C5596"), new dimple.color("#CA9A9A"), new dimple.color("#D8E4EA"),
                                            new dimple.color("#326277"), new dimple.color("#9174A5"), new dimple.color("#7B0404"), new dimple.color("#EAE2EF"),
                                            new dimple.color("#562323"), new dimple.color("#03671F"), new dimple.color("#7b6888"), new dimple.color("#E3F25E"),
                                            new dimple.color("#F498DA"), new dimple.color("#6b486b") ];
				barChart.setBounds('10%', '10%', '85%', '73%');
                var x = barChart.addCategoryAxis("x", "Activity");
				if (metric == "Number of Instances") {
                    var y = barChart.addMeasureAxis("y", "Instances");
                    x.addOrderRule("Instances", true);
                }
                else {
                    var y = barChart.addMeasureAxis("y", "Hours");
                    y.tickFormat = ',.2f';
                    x.addOrderRule("Hours", true);
                }
                x.title = "Activities in desc order of Metric";
				barChart.addSeries("Activity", dimple.plot.bar);
                barChart.draw();
                chartOuter.draw();
                chartInner.draw();

                $('select[name="metric-select"]').off().on('change', function() {
					var metric = $('#metric-select').val();
					if ( metric == "Number of Instances") {
						outer_p.measure = "Instances";
						inner_p.measure = "Instances";
                        y.measure = "Instances";
                        y.tickFormat = '';
                        x._orderRules[0].ordering = "Instances";
					}
					else{
						outer_p.measure = "Hours";
						inner_p.measure = "Hours";
                        y.measure = "Hours";
                        y.tickFormat = ',.2f';
                        x._orderRules[0].ordering = "Hours";
					}
					chartOuter.draw();
					chartInner.draw();
                    barChart.draw();
    			});

                $(window).on('resize', function() {

                    chartOuter.draw(0, true);
                    chartInner.draw(0, true);
                    barChart.draw(0, true);
                });

			}
	    });
     };

 /**************************************************************************************/
    function OneActivityAllFriends() {
    	var activity_chosen = $('#activity-select').val();
        var range = $('#dateRange').val();
        var metric = $('#metric-select').val();
        $('.analytics-topChart h1').text('Friend Distribution');
        $('.analytics-bottomChart h1').text('Timeorder Friend Analysis');
		$.ajax({
			type: "post",
			data: {activity: activity_chosen, csrfmiddlewaretoken: getCookie('csrftoken'), range: range},
			cache: false,
			url: BASE_URL + 'analytics/friends/update/activity_friends/',
			dataType: "json",
			error: function (xhr, status, error) {
				Done();
				console.log('went bad');
			},
			success: function (response) {
                try {
                    svg.selectAll('*').remove();
                    svg2.selectAll('*').remove();
                }
                catch(err) {}
                var donutChart = new dimple.chart(svg, response[0]);
                donutChart.setBounds('5%', '10%', '80%', '80%');


                if ( metric == "Number of Instances") {
                   var outer_p = donutChart.addMeasureAxis("p", "Instances");
				}
                else{
                  var  outer_p = donutChart.addMeasureAxis("p", "Hours");
                }
                donutChart.addLegend("85%", 20, 90, 300, "left");
                var outerRing = donutChart.addSeries("Friend", dimple.plot.pie);
				outerRing.innerRadius = "-30px";

				var barChart = new dimple.chart(svg2, response[1]);
				barChart.setBounds('5%', '10%', '85%', '70%');
				var y = barChart.addMeasureAxis("y", "Hours");
                y.tickFormat = ',.2f';
				var x = barChart.addCategoryAxis("x", ["Start_Date", "Friend"]);
                x.addOrderRule("Timeorder");
                x.title = "Instances in order of time";
				barChart.addSeries("Friend", dimple.plot.bar);
                barChart.addLegend("10%", 0, "80%", 40, "right");
                donutChart.defaultColors = [new dimple.color("#98abc5"), new dimple.color("#8a89a6"), new dimple.color("#ff8c00"),new dimple.color("#995411"),
                                            new dimple.color("#7b6888"), new dimple.color("#E07C27"), new dimple.color("#a05d56"), new dimple.color("#d0743c"),
                                            new dimple.color("#7b6888"), new dimple.color("#266419"), new dimple.color("#DF7821"), new dimple.color("#4DA4DA"),
                                            new dimple.color("#A5C59E"), new dimple.color("#5C5596"), new dimple.color("#CA9A9A"), new dimple.color("#D8E4EA"),
                                            new dimple.color("#326277"), new dimple.color("#9174A5"), new dimple.color("#7B0404"), new dimple.color("#EAE2EF"),
                                            new dimple.color("#562323"), new dimple.color("#03671F"), new dimple.color("#7b6888"), new dimple.color("#E3F25E"),
                                            new dimple.color("#F498DA"), new dimple.color("#6b486b") ];
                barChart.defaultColors = [new dimple.color("#98abc5"), new dimple.color("#8a89a6"), new dimple.color("#ff8c00"),new dimple.color("#995411"),
                                            new dimple.color("#7b6888"), new dimple.color("#E07C27"), new dimple.color("#a05d56"), new dimple.color("#d0743c"),
                                            new dimple.color("#7b6888"), new dimple.color("#266419"), new dimple.color("#DF7821"), new dimple.color("#4DA4DA"),
                                            new dimple.color("#A5C59E"), new dimple.color("#5C5596"), new dimple.color("#CA9A9A"), new dimple.color("#D8E4EA"),
                                            new dimple.color("#326277"), new dimple.color("#9174A5"), new dimple.color("#7B0404"), new dimple.color("#EAE2EF"),
                                            new dimple.color("#562323"), new dimple.color("#03671F"), new dimple.color("#7b6888"), new dimple.color("#E3F25E"),
                                            new dimple.color("#F498DA"), new dimple.color("#6b486b") ];
                barChart.draw();
                donutChart.draw();

                $('select[name="metric-select"]').off().on('change', function() {
					var metric = $('#metric-select').val();
					if ( metric == "Number of Instances") {
						outer_p.measure = "Instances";
					}
					else{
						outer_p.measure = "Hours";
					}
					donutChart.draw();
    			});

                $(window).on('resize', function() {
                    donutChart.draw(0, true);
                    barChart.draw(0, true);
                });
			}
	    });
    };

 /**************************************************************************************/
    function OneActivityOneFriend() {
    	var activity_chosen = $('#activity-select').val();
        var friend_chosen = $('#friend-select').val();
        var range = $('#dateRange').val();
        $('.analytics-bottomChart h1').text('');
        $('.analytics-topChart h1').text('Instance Tracking');
		$.ajax({
			type: "post",
			data: {activity: activity_chosen, friend: friend_chosen, csrfmiddlewaretoken: getCookie('csrftoken'), range: range},
			cache: false,
			url: BASE_URL + 'analytics/friends/update/activity_friend/',
			dataType: "json",
			error: function (xhr, status, error) {
				Done();
				console.log('went bad');
			},
			success: function (response) {
                try {
                    svg.selectAll('*').remove();
                    svg2.selectAll('*').remove();
                }
                catch(err) {}
                var color_dict = {'0': "#C0BBBB", '1': "red", '2': "yellow", '3': "green"};
                var goal_dict = {'0': "n/a", '1': "Failed", '2': "In Progress", '3': "Reached"};
                var lineChart = new dimple.chart(svg, response);
                lineChart.setBounds('10%', '10%', '85%', '80%');
                lineChart.addMeasureAxis("y", "Hours");

                var x = lineChart.addCategoryAxis("x", "Start_Date");
                x.addOrderRule("Timeorder");
                x.title = "Instances ordered by Date";
                if ((response.length > 1) && (!AllSameStatus(response))) {
                    var goal_status_prices_exist = {"0": 0, "1": 0, "2": 0, "3":0 };
                    var goal_status_color_list = [];
                    $.each(response, function(i, e) {
                           goal_status_prices_exist[e.Goal_Status.toString()] = 1;
                    });
                    if (goal_status_prices_exist["0"] == 1)
                        goal_status_color_list.push("#C0BBBB");
                    if (goal_status_prices_exist["1"] == 1)
                        goal_status_color_list.push("red");
                    if (goal_status_prices_exist["2"] == 1)
                        goal_status_color_list.push("yellow");
                    if (goal_status_prices_exist["3"] == 1)
                        goal_status_color_list.push("green");

                    lineChart.addColorAxis("Goal_Status", goal_status_color_list);
                    var lines = lineChart.addSeries(null, dimple.plot.line);
                }
                else {
                    var lines = lineChart.addSeries("Line", dimple.plot.line);
                    if (response.length > 0) {
                        lineChart.assignColor('Line', color_dict[response[0].Goal_Status])
                    }
                }
                lines.lineWeight = 5;
                lines.lineMarkers = true;

                lines.getTooltipText = function (e) {
                   if (response.length == 1) {
                       e.cValue = response[0].Goal_Status;
                   }
                   return ["Date Started: " + e.x, "Hours: " + e.yValue, "Goal: " + goal_dict[e.cValue]]
                };

                lineChart.draw();

                $(window).on('resize', function() {
                    lineChart.draw(0, true);
                });

                function AllSameStatus(list){
                    var flag = true;
                    try {
                        var status = list[0].Goal_Status
                    }
                    catch(err) {
                        return true;
                    }
                    $.each(list, function(i, e) {
                        if (e.Goal_Status != status) {
                            flag = false;
                        }
                    });
                    if (flag) {
                        return true;
                    }
                    else {
                        return false;
                    }
                }
			}
	    });
    };

 /**************************************************************************************/
    function AllActivitiesAllFriends() {
        Loading();
        var range = $('#dateRange').val();
        var metric = $('#metric-select').val();
        $('.analytics-bottomChart h1').text('');
        $('.analytics-topChart h1').text('Friends/Activities Intensity');
		$.ajax({
			type: "post",
			data: { csrfmiddlewaretoken: getCookie('csrftoken'), range: range},
			cache: false,
			url: BASE_URL + 'analytics/friends/update/activities_friends/',
			dataType: "json",
			error: function (xhr, status, error) {
				Done();
				console.log('went bad');
			},
			success: function (response) {
                try {
                    svg.selectAll('*').remove();
                    svg2.selectAll('*').remove();
                }
                catch(err) {}

                var bubbleChart = new dimple.chart(svg, response);
                bubbleChart.setBounds('10%', '10%', '85%', '80%');
                var x = bubbleChart.addCategoryAxis("x", "Friend");
                var y = bubbleChart.addCategoryAxis("y", "Activity");
                if ( metric == "Number of Instances") {
                   var z = bubbleChart.addMeasureAxis("z", "Instances");
				}
                else {
                   var z = bubbleChart.addMeasureAxis("z", "Hours");
                }
                var bubbleSeries = bubbleChart.addSeries("Friend", dimple.plot.bubble);
                bubbleSeries.radius = "30";
                bubbleChart.defaultColors = [new dimple.color("#98abc5"), new dimple.color("#8a89a6"), new dimple.color("#ff8c00"),new dimple.color("#995411"),
                                            new dimple.color("#7b6888"), new dimple.color("#E07C27"), new dimple.color("#a05d56"), new dimple.color("#d0743c"),
                                            new dimple.color("#7b6888"), new dimple.color("#266419"), new dimple.color("#DF7821"), new dimple.color("#4DA4DA"),
                                            new dimple.color("#A5C59E"), new dimple.color("#5C5596"), new dimple.color("#CA9A9A"), new dimple.color("#D8E4EA"),
                                            new dimple.color("#326277"), new dimple.color("#9174A5"), new dimple.color("#7B0404"), new dimple.color("#EAE2EF"),
                                            new dimple.color("#562323"), new dimple.color("#03671F"), new dimple.color("#7b6888"), new dimple.color("#E3F25E"),
                                            new dimple.color("#F498DA"), new dimple.color("#6b486b") ];

                x.showGridlines = true;
                y.showGridlines = true;
                Done();
                bubbleChart.draw();


                $('select[name="metric-select"]').off().on('change', function() {
					var metric = $('#metric-select').val();
					if ( metric == "Number of Instances") {
						z.measure = "Instances";
					}
					else{
						z.measure = "Hours";
					}
					bubbleChart.draw();
    			});

                $(window).on('resize', function() {
                    bubbleChart.draw(0, true);
                });
			}
	    });
    }


    function updateFriendsBanner(activity_selected, friend_selected) {
        var range = $('#dateRange').val();
        $.ajax({
            type: "post",
            data: {range: range, csrfmiddlewaretoken: getCookie('csrftoken'), friend: friend_selected, activity: activity_selected},
            cache: false,
            url: BASE_URL + 'analytics/friends/update/friends_chartbanner/',
            dataType: "json",
            error: function (xhr, status, error) {
                Done();
                console.log('went bad');
            },
            success: function (response) {
                $('#totalActivities').text(response.total_activities);
                $('#totalActivitiesWithFriends').text(response.total_activities_done_with_friends);
                $('#totalParticipationOfFriends').text(response.percentage_of_activities_with_friends.toFixed(1) + "%");
                $('#totalTimeWithFriends').text(response.total_time_spent_with_friends);
                $('#date-range-total-analytics').text(range);

                if ((activity_selected == "all") && (friend_selected == "all")) {
                    $('#totalActivitiesLabel').text("Total Activities performed:");
                    $('#totalActivitiesWithFriendsLabel').text("Total Activities done with Friends:");
                    $('#totalParticipationOfFriendsLabel').text("Total Participation of Friends:");
                    $('#totalTimeWithFriendsLabel').text("Total Time spent with Friends:");
                }
                else if ((activity_selected == "all") && (friend_selected != "all")) {
                    $('#totalActivitiesLabel').text("Total Activities performed:");
                    if (friend_selected != "") {
                        $('#totalActivitiesWithFriendsLabel').text("Activities with selected Friend:");
                        $('#totalParticipationOfFriendsLabel').text("Participation of selected Friend:");
                        $('#totalTimeWithFriendsLabel').text("Time spent with selected Friend:");
                    }
                    else{
                        $('#totalActivitiesWithFriendsLabel').text("Activities done Alone:");
                        $('#totalParticipationOfFriendsLabel').text("Activity percentage done Alone:");
                        $('#totalTimeWithFriendsLabel').text("Time spent on Activities Alone:");
                    }
                }
                else if ((activity_selected != "all") && (friend_selected == "all")) {
                    $('#totalActivitiesLabel').text("Total Instances of Activity:");
                    $('#totalActivitiesWithFriendsLabel').text("Total Instances done with Friends:");
                    $('#totalParticipationOfFriendsLabel').text("Total Participation of Friends");
                    $('#totalTimeWithFriendsLabel').text("Total Time spent with Friends:");
                }
                else {
                    $('#totalActivitiesLabel').text("Total Instances of Activity:");
                    if (friend_selected != "") {
                        $('#totalPercentageWithFriendsLabel').text("Instances with selected Friend:");
                        $('#totalParticipationOfFriendsLabel').text("Participation of selected Friend:");
                        $('#totalTimeWithFriendsLabel').text("Time spent with selected Friend:");
                    }
                    else{
                        $('#totalActivitiesWithFriendsLabel').text("Instances done Alone:");
                        $('#totalParticipationOfFriendsLabel').text("Instance percentage done Alone:");
                        $('#totalTimeWithFriendsLabel').text("Time spent on Instances Alone:");
                    }
                }
            }
        });
    }



    $('#dateRange').val('01/01/2015 - ' + moment().format("MM/DD/YYYY"));
	$('#dateRange').daterangepicker({
		format: 'MM/DD/YYYY',
		startDate: moment().startOf('year'),
		endDate: moment(),
		ranges: {
		   'Today': [moment(), moment()],
		   'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
		   'Previous Week': [moment().subtract(1, 'week').startOf('week').add(1,'day'), moment().subtract(1,'week').endOf('week').add(1,'day')],
		   'Previous Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')],
           'Month to Date': [moment().startOf('month'), moment()],
           'Year to Date': [moment().startOf('year'), moment()]
		},
		locale: {
			monthNames: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
			fromLabel: 'From',
			toLabel: 'To',
			customRangeLabel: 'Custom Range'
		}
	});


    $(window).on('load', function(){
        $('#dateRange').trigger('change');
    });
