import uuid     
import json      
import logging   
from pprint import pprint  


# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv(override=True)  

# Import the main workflow graph (the "brain" of compliance system)
from backend.src.graph.workflow import app

# Configure logging 
logging.basicConfig(
    level=logging.INFO,        
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  
)
logger = logging.getLogger("ComplianceQAPipeline")  # Creates a named logger for this module


def run_cli_simulation():
   
    session_id = str(uuid.uuid4())  # uuid4() generates random UUID
    logger.info(f"Starting Audit Session: {session_id}")  # Log to console/file


    initial_inputs = {
        # The YouTube video to audit
        "video_url": "https://youtu.be/dT7S75eYhcQ",
        
        "video_id": f"vid_{session_id[:8]}",
        
        "compliance_results": [],
        
    
        "errors": []
    }

    print("\n--- 1.nput Payload: INITIALIZING WORKFLOW ---")
    
    print(f"I {json.dumps(initial_inputs, indent=2)}")


    try:
    
        final_state = app.invoke(initial_inputs)
        
        print("\n--- 2. WORKFLOW EXECUTION COMPLETE ---")
        
        print("\n=== COMPLIANCE AUDIT REPORT ===")
        
        print(f"Video ID:    {final_state.get('video_id')}")
    
        print(f"Status:      {final_state.get('final_status')}")
        
        print("\n[ VIOLATIONS DETECTED ]")
        
        results = final_state.get('compliance_results', [])
        
        if results:
            for issue in results:
                print(f"- [{issue.get('severity')}] {issue.get('category')}: {issue.get('description')}")
        else:
            print("No violations found.")

        print("\n[ FINAL SUMMARY ]")
        print(final_state.get('final_report'))

    except Exception as e:
        logger.error(f"Workflow Execution Failed: {str(e)}")
        raise e


if __name__ == "__main__":
    run_cli_simulation()  