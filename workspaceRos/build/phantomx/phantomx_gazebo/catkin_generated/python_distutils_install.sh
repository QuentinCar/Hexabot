#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/cyril/Documents/uv5.8/Hexabot/workspaceRos/src/phantomx/phantomx_gazebo"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/cyril/Documents/uv5.8/Hexabot/workspaceRos/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/cyril/Documents/uv5.8/Hexabot/workspaceRos/install/lib/python2.7/dist-packages:/home/cyril/Documents/uv5.8/Hexabot/workspaceRos/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/cyril/Documents/uv5.8/Hexabot/workspaceRos/build" \
    "/usr/bin/python2" \
    "/home/cyril/Documents/uv5.8/Hexabot/workspaceRos/src/phantomx/phantomx_gazebo/setup.py" \
    build --build-base "/home/cyril/Documents/uv5.8/Hexabot/workspaceRos/build/phantomx/phantomx_gazebo" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/cyril/Documents/uv5.8/Hexabot/workspaceRos/install" --install-scripts="/home/cyril/Documents/uv5.8/Hexabot/workspaceRos/install/bin"
