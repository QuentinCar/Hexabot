#include <ros/ros.h>
#include <visualization_msgs/Marker.h>

#include <cmath>

#include <phantomx_gazebo/Rifts.h>

//Global variable
visualization_msgs::Marker points;
ros::Publisher marker_pub;


void pointsCallback(const phantomx_gazebo::Rifts::ConstPtr &msg)
{
	geometry_msgs::Point p;
	
	
	//for (int i=0; i<(sizeof(msg->x)/sizeof(msg->x[0])); i++){
	if(!(msg->x).empty()){
		int i=0;
		while((msg->x)[i] != '\0'){
			p.x = (msg->x)[i];
			p.y = (msg->y);
			p.z = (msg->z)[i];

			if (abs(p.x) < 100 && abs(p.z) < 100 && abs(p.x) > 1.5) {
				if (abs(p.x) < 5){
					ROS_INFO("Rift Found : %f, %f, %f", p.x, p.y, p.z);
				}
				points.points.push_back(p);
			}
			
			i++;

		}
	}
	
	marker_pub.publish(points);
	        
}


int main( int argc, char** argv )
{

	ROS_INFO("Start Up marker_display.cpp");

	ros::init(argc, argv, "rift_points");
	ros::NodeHandle n;
	marker_pub = n.advertise<visualization_msgs::Marker>("visualization_marker", 10);
	ros::Subscriber sub = n.subscribe("/phantomx/rifts_coord", 10, pointsCallback);


	points.header.frame_id  = "map";
	points.header.stamp = ros::Time::now();
	points.ns = "rift_points";
	points.action = visualization_msgs::Marker::ADD;
	points.pose.orientation.w = 1.0;


	points.id = 0;


	points.type = visualization_msgs::Marker::POINTS;


	// POINTS markers use x and y scale for width/height respectively
	points.scale.x = 0.1;
	points.scale.y = 0.1;

	// Points are green
	points.color.g = 1.0f;
	points.color.a = 1.0;

	ros::spin();


}

