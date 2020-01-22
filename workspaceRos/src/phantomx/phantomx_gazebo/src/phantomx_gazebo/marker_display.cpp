#include <ros/ros.h>
#include <visualization_msgs/Marker.h>

#include <cmath>

#include <phantomx_gazebo/Fissures>

//Global variable
visualization_msgs::Marker points;


void pointsCallback(const phantomx_gazebo::Fissures::ConstPtr& msg)
{

	geometry_msgs::Point p;
	//Update points (cast possible ??)
	p.x = msg.x;
	p.y = msg.y;
	p.z = msg.z;

	points.points.push_back(p);
}


int main( int argc, char** argv )
{
	ros::init(argc, argv, "points_and_lines");
	ros::NodeHandle n;
	ros::Publisher marker_pub = n.advertise<visualization_msgs::Marker>("visualization_marker", 10);

	ros::Subscriber sub = n.subscribe("node_name", 1000, pointsCallback);


	points.header.frame_id  = "/base_link";
	points.header.stamp = ros::Time::now();
	points.ns = "points_and_lines";
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



	ros::Rate r(30);

  while (ros::ok())
  {


    marker_pub.publish(points);

    r.sleep();

  }
}

