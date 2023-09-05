using UnityEngine;
using Unity.MLAgents;
using Unity.MLAgents.Sensors;
using Unity.MLAgents.Actuators;
using System.Collections.Generic;
using System.Diagnostics.Contracts;

public class ml_test : Agent
{

    //[SerializeField] private Transform enemy;
    //private Rigidbody rBody;

    public List<Transform> enemies;

    [SerializeField] private float speed = 3f;

    private float totalReward = 0f;

    private int currentEnemyIndex = 0;

    public spawn_manager spawner;

/*
    public void Awake()
    {
        rBody = GetComponent<Rigidbody>();
    }
*/

    public override void OnEpisodeBegin()
    {
        transform.position = new Vector3(0f, 1.73f, 0f);
        currentEnemyIndex = 0;
        totalReward = 0f;
        DestroyAllEnemies();
    }
 

    public override void CollectObservations(VectorSensor sensor)
    {
        //sensor.AddObservation(transform.position);
        Vector3 combinedObservation = new Vector3(transform.position.x, transform.position.y, transform.position.z);
        combinedObservation += enemies[currentEnemyIndex].position;
        sensor.AddObservation(combinedObservation);
    }

    public override void OnActionReceived(ActionBuffers actions)
    {

        float moveX = actions.ContinuousActions[0];
        float moveZ = actions.ContinuousActions[1];

        Vector3 moveDirection = new Vector3(moveX, 0, moveZ);

        //transform.Translate(moveDirection * Time.deltaTime * speed);

        transform.position += new Vector3(moveX, 0, moveZ) * Time.deltaTime * speed;


        float distanceToEnemy = Vector3.Distance(transform.position, enemies[currentEnemyIndex].position);

        if (distanceToEnemy < 1.0f)
        {

            AddReward(-0.1f);
        }

        AddReward(0.01f);

        totalReward += GetCumulativeReward();
    }

    public override void Heuristic(in ActionBuffers actionsOut)
    {
        Debug.Log("called");
        ActionSegment<float> Caction = actionsOut.ContinuousActions;
        Caction[0] = Input.GetAxisRaw("Horizontal");
        Caction[1] = Input.GetAxisRaw("Vertical");
        Debug.Log("Caction[0]: " + Caction[0]);
        Debug.Log("Caction[1]: " + Caction[1]);
    }


    public void addEnemy()
    {
        currentEnemyIndex++;
    }

    private void OnCollisionEnter(Collision other)
    {
        Debug.Log("touch");

        if (other.gameObject.CompareTag("enemy"))
        {
            Debug.Log("touch enemy");
            AddReward(-1f);
            EndEpisode();
            spawner.resetNumber();
        }
    }

    public void DestroyAllEnemies()
    {

        foreach (Transform enemy in enemies)
        {
            if (enemy != null)
            {
                Destroy(enemy.gameObject);
            }
        }
        enemies.Clear();
    }

}
