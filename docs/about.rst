About GTFS
==========

GTFS (*General Transit Feed Specification*) was developed for...

.. note::

    GTFS is a specification, not a database. It is a set of rules that define how transit agencies should publish their data. The data itself is published in a set of CSV-like files.

.. important::

    This package uses GTFS revised May 9, 2022. 

GTFS Schedule
    Includes agency information and 

GTFS Realtime
    Collects and publishes information from on-board equipments like GPS for real-time location, and also from administrative entities, like agencies and emergency services, for service updates and service alerts.

GTFS Schedule
-------------

This is the information.

GTFS Realtime
-------------

GTFS Realtime provides 

- data generated from on-board equipment including real-time location

Structure of a message:

- header
    - gtfs_realtime_version
    - incrementality
    - timestamp
- entity
    - id
    - is_deleted
    - trip_update
    - vehicle
    - alert
    - shape

In this sense, a single ``FeedMessage`` contains a ``FeedHeader`` and one or many ``FeedEntity``.

There are three supported entities:

- ``TripUpdate``
- ``VehiclePosition``
- ``Alert``

This package obtains information from the ``VehiclePosition`` entity.

The entity ``VehiclePosition`` contains the following fields:

- ``trip``: The Trip that this vehicle is serving. Can be empty or partial if the vehicle can not be identified with a given trip instance.
- ``vehicle``: Additional information on the vehicle that is serving this trip.
- ``position``: The current position of this vehicle.
- ``current_stop_sequence``: The stop sequence index of the current stop. The meaning of ``current_stop_sequence`` (i.e., the stop that it refers to) is determined by ``current_status``. If ``current_status`` is missing, ``IN_TRANSIT_TO`` is assumed.
- ``stop_id``: The ID of the current stop. Must be the same as in stops.txt in the corresponding GTFS feed.
- ``current_status``: The exact status of the vehicle with respect to the current stop. Ignored if ``current_stop_sequence`` is missing.
- ``timestamp``: Moment at which the vehicle's position was measured. In POSIX time (i.e., number of seconds since January 1st 1970 00:00:00 UTC).
- ``congestion_level``: Traffic congestion level that is affecting this vehicle.
- ``occupancy_status``: The degree of passenger occupancy of the vehicle.
- ``occupancy_percentage``: The degree of passenger occupancy of the vehicle as a percentage. This field is an alternative to ``occupancy_status``, and will take precedence if both are populated. Valid values are between 0 and 100, inclusive.

Along with the ``timestamp``, any of these values can be used to create a time series or filter it.

For example: the package can create a time series containing the occupancy percentage of a vehicle for a certain trip.

That is:

1. Filter by X values
2. Index with timestamp
3. Add Y values



Timestamps: ``FeedHeader.timestamp``, ``FeedEntity.vehicle.timestamp`` and ``FeedEntity.trip_update.timestamp`` are available for the creation of a time series.

Service alerts do not have a specific timestamp (other than that of the Realtime message itself).



The ``timestamp`` field is the time when the data was generated. The ``incrementality`` field indicates whether the ``FeedMessage`` is a complete snapshot of the data or whether it is incremental.

GTFS v2.0 divides Realtime data into three categories, or "Feed Entities":

Trip Updates
    *"Bus X is delayed by 5 minutes"*

    Represent fluctuations in the timetable.

Service Alerts
    *"Station Y is closed due to construction"*

    Represent higher level problems with a particular entity and are generally in the form of a textual description of the disruption.

Vehicle Positions
    *"This bus is at position X at time Y"*

    Represents a few basic pieces of information about a particular vehicle on the network.


Trip Updates
^^^^^^^^^^^^

Trip updates are used to provide real-time information about the status of a vehicle in transit. This includes the vehicle's current stop, the next stop, and the status of the vehicle (e.g., in transit to the next stop, delayed, etc.).

- ``TripDescriptor``
- ``VehicleDescriptor``
- ``StopTimeUpdate``

Service Alerts
^^^^^^^^^^^^^^

Service alerts are used to provide real-time information about service disruptions, planned service changes, and other service-related events. These are typically used to provide information about planned service changes, such as detours, route closures, and schedule changes. They can also be used to provide information about unplanned service disruptions, such as traffic accidents, weather-related events, and other service-related events.

- ``TimeRange``
- ``EntitySelector``
    - ``TripDescriptor``
- ``Cause``
- ``Effect``
- ``SeverityLevel``

Vehicle Position
^^^^^^^^^^^^^^^^

Vehicle positions are used to provide real-time information about the location of vehicles in transit. This information is typically used to provide information about the location of vehicles on a route, and to provide information about the status of vehicles (e.g., in transit to the next stop, delayed, etc.).

- ``TripDescriptor``
- ``VehicleDescriptor``
- ``Position``
- ``VehicleStopStatus``
- ``CongestionLevel``
- ``OccupancyStatus``
- ``CarriageDetails``
