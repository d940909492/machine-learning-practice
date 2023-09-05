using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.MLAgents;
using Unity.MLAgents.Actuators;
using Unity.MLAgents.Sensors;
using static UnityEngine.GraphicsBuffer;

public class test_ai : Agent
{

    //[SerializeField] private Transform Targettranform;
    public override void OnEpisodeBegin()
    {
        transform.position = new Vector3(0f,1.5f,0f);
    }

    public override void CollectObservations(VectorSensor sensor)
    {
        sensor.AddObservation(transform.position);
    }

    public override void OnActionReceived(ActionBuffers actions)
    {
        float movex = actions.ContinuousActions[0];
        float movez = actions.ContinuousActions[1];

        float movespeed = 3f;
        transform.position += new Vector3(movex, 0, movez) * Time.deltaTime * movespeed;
    }

    public override void Heuristic(in ActionBuffers actionsOut)
    {
        ActionSegment<float> continuousActions = actionsOut.ContinuousActions;

        continuousActions[0] = Input.GetAxisRaw("Horizontal");
        continuousActions[1] = Input.GetAxisRaw("Vertical");
    }

}
