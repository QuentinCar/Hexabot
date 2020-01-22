#include <ros/ros.h>
#include <visualization_msgs/Marker.h>

#include <cmath>

#include <phantomx_gazebo/Fissures.h>

//Global variable
visualization_msgs::Marker points;
ros::Publisher marker_pub;


void pointsCallback(const phantomx_gazebo::Fissures::ConstPtr &msg)
{

	geometry_msgs::Point p;
	
		for (int i=0; i< sizeof(msg->x); i++){
			p.x = (msg->x)[i];
			p.y = (msg->y);
			p.z = (msg->z)[i];

			points.points.push_back(p);

	}
	
	marker_pub.publish(points);
	        
}


int main( int argc, char** argv )
{

	ros::init(argc, argv, "rift_points");
	ros::NodeHandle n;
	marker_pub = n.advertise<visualization_msgs::Marker>("visualization_marker", 10);
	ros::Subscriber sub = n.subscribe("/phantomx/rifts_coord", 1000, pointsCallback);


	points.header.frame_id  = "/base_link";
	points.header.stamp = ros::Time::now();
	points.ns = "rift_points";
	points.action = visualization_msgs::Marker::ADD;
	points.pose.orientation.w = 1.0;


	points.id = 0;


	points.type = visualization_msgs::Marker::POINTS;


	// POINTS markers use x and y scale for width/height respectively
	points.scale.x = 0.2;
	points.scale.y = 0.2;

	// Points are green
	points.color.g = 1.0f;
	points.color.a = 1.0;

	ros::spin();


}

