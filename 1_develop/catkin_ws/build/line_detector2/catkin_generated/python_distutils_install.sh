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

echo_and_run cd "/duckietown/catkin_ws/src/dt-core/packages/line_detector2"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/duckietown/catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/duckietown/catkin_ws/install/lib/python2.7/dist-packages:/duckietown/catkin_ws/build/line_detector2/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/duckietown/catkin_ws/build/line_detector2" \
    "/usr/bin/python2" \
    "/duckietown/catkin_ws/src/dt-core/packages/line_detector2/setup.py" \
    build --build-base "/duckietown/catkin_ws/build/line_detector2" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/duckietown/catkin_ws/install" --install-scripts="/duckietown/catkin_ws/install/bin"
