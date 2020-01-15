#include <ros/ros.h>
#include <visualization_msgs/Marker.h>

#include <cmath>

//Global variable
visualization_msgs::Marker points;


void pointsCallback(/*Point Value*/){

      geometry_msgs::Point p;
      p.x = x;
      p.y = y;
      p.z = z;

      points.points.push_back(p);

}


int main( int argc, char** argv )
{
  ros::init(argc, argv, "marker");
  ros::NodeHandle n;
  ros::Publisher marker_pub = n.advertise<visualization_msgs::Marker>("visualization_marker", 10);

  ros::Subscriber sub = n.subscribe("node_name", 1000, pointsCallback);

  ros::Rate r(30);

  float f = 0.0;
  while (ros::ok())
  {

    //Initialise point
    points.header.frame_id = "/base_link";
    points.header.stamp = ros::Time::now();
    points.ns = "marker";
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


    marker_pub.publish(points);

    r.sleep();

  }
}

