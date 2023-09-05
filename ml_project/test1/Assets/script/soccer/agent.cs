using UnityEngine;
using Unity.MLAgents;
using Unity.MLAgents.Sensors;
using Unity.MLAgents.Actuators;

public class SoccerAgent : Agent
{
    public GameObject ball;
    public float speed = 5f;
    private bool wantsToPass;
    private GameObject teammate;

    public override void Initialize()
    {
    
        ball = GameObject.FindWithTag("Ball");
        teammate = GameObject.FindWithTag("Teammate");
    }

    public override void OnEpisodeBegin()
    {
   
    }

    public override void CollectObservations(VectorSensor sensor)
    {
  
        sensor.AddObservation(transform.position);
        sensor.AddObservation(ball.transform.position);
        sensor.AddObservation(teammate.transform.position);
    }

    public override void OnActionReceived(ActionBuffers vectorAction)
    {
        var continuousActions = vectorAction.ContinuousActions;
        float moveX = continuousActions[0];
        float moveZ = continuousActions[1];

        var discreteActions = vectorAction.DiscreteActions;
        bool wantsToPass = discreteActions[0] > 0;

        Vector3 moveDirection = new Vector3(moveX, 0f, moveZ).normalized;
        transform.Translate(moveDirection * speed * Time.deltaTime);

   
        if (wantsToPass && Vector3.Distance(transform.position, teammate.transform.position) < 1.0f)
        {
            PassBall();
        }

    }

    private void PassBall()
    {
        ball.GetComponent<BallController>().PassTo(teammate);
    }
}
