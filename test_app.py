#!/usr/bin/env python3
"""
Simple test script to verify the Flask app is working in broken mode
"""

import requests
import time

def test_app():
    """Test the Flask app to see if it's in broken mode"""
    print("🧪 Testing Flask Todo App...")
    print("=" * 40)
    
    # Wait a moment for the app to fully start
    time.sleep(2)
    
    try:
        # Test the root route (should show setup instructions)
        print("Testing root route (/)...")
        response = requests.get("http://127.0.0.1:5000/", timeout=5)
        
        if response.status_code == 200:
            content = response.text
            if "Database Setup Required" in content:
                print("✅ Root route working - shows setup instructions")
            else:
                print("❌ Root route not showing setup instructions")
                print("Content preview:", content[:200])
        else:
            print(f"❌ Root route returned status code: {response.status_code}")
            
        # Test login route (should show database error)
        print("\nTesting login route (/login)...")
        response = requests.get("http://127.0.0.1:5000/login", timeout=5)
        
        if response.status_code == 200:
            content = response.text
            if "Database Error" in content or "Database tables do not exist" in content:
                print("✅ Login route working - shows database error")
            else:
                print("❌ Login route not showing database error")
                print("Content preview:", content[:200])
        else:
            print(f"❌ Login route returned status code: {response.status_code}")
            
        # Test register route (should show database error)
        print("\nTesting register route (/register)...")
        response = requests.get("http://127.0.0.1:5000/register", timeout=5)
        
        if response.status_code == 200:
            content = response.text
            if "Database Error" in content or "Database tables do not exist" in content:
                print("✅ Register route working - shows database error")
            else:
                print("❌ Register route not showing database error")
                print("Content preview:", content[:200])
        else:
            print(f"❌ Register route returned status code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the Flask app")
        print("Make sure the app is running with: python app.py")
    except Exception as e:
        print(f"❌ Error testing app: {e}")
    
    print("\n" + "=" * 40)
    print("🎯 Expected Result: All routes should show database errors")
    print("This means the lab is working correctly!")

if __name__ == "__main__":
    test_app()
