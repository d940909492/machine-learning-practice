using UnityEngine;
using TMPro;

public class showreward : MonoBehaviour
{
    public ml_test mlAgent;
    private TextMeshPro textMeshPro;

    private void Start()
    {
        textMeshPro = GetComponent<TextMeshPro>();
        UpdateRewardText();
    }

    private void Update()
    {

        UpdateRewardText();
    }

    private void UpdateRewardText()
    {
        if (mlAgent != null)
        {
            textMeshPro.text = "Rewards Earned: " + mlAgent.totalReward.ToString("F2");
        }
    }
}
