# What will be needed in the ports area, considering the arch style?
- We need the message queue/broker connection and a producer/listener on our side.
Producer will be implemented using the above to create an analyze_weather event
Listener will gather information received via weather_analysis_topic with matching event_id.
- Possibly a fun weather related texts as an entertaining element to the waiting process
- The handling will be based on receiving updates and waiting a certain amount, if the update doesn't come, a 
relaxing message and "pulse" will be transmitted to the webapp to provide "responsibility" and to make the user feel as
there is indeed something happening and the system is alive and well.
- There can be a second producer which will handle creating timing analysis data and broadcasting it via some topic. Without response, one way pipeline.