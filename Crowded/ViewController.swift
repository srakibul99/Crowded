//
//  ViewController.swift
//  thronged
//
//  Created by Shakira Rakibullah on 7/29/20.
//  Copyright © 2020 thronged. All rights reserved.
//

import UIKit
import CoreLocation

class ViewController: UIViewController {
    
    @IBOutlet weak var locationField: UITextField!
    
    @IBOutlet weak var queryField: UITextField!
    
    @IBOutlet weak var resultsLabel: UILabel!
    
    @IBOutlet weak var results2Label: UILabel!
    
    @IBOutlet weak var results3Label: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func onTap(_ sender: Any) {
        view.endEditing(true)
    }
    
    @IBAction func getResults(_ sender: Any) {
        
        // get location, get query
        
        let location = locationField.text! ?? ""
        let query = queryField.text! ?? ""
        
        /*
        var VenueOne:String?
        var VenueTwo:String?
        var VenueThree:String?
         
         https:// api.foursquare.com/v2/venues/search?near=\(location)&v=20200607&intent=checkin&limit=3&radius=4000&client_id=\(CLIENT_ID)&client_secret=\(CLIENT_SECRET)&query=\(query))
 */
        // call API and find top 3 results
        // url - 4square explore
        let CLIENT_ID = ""
        let CLIENT_SECRET = ""
        
        /**
        if let url = URL(string:  "https ://api.foursquare.com/v2/venues/explore?near=SanJose,CA&v=20200607&limit=3&client_id=UNXKPYYYPY2PQFGNYL3KXWTKGNT20SO4ISO0YDROW0HORX2W&client_secret=QWPXY050I0NWIEIGIGHGNUBM0XXWN42SNS2XGBGKL3RXBKP3&query=coffee") {
            let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
                
                if let data = data {
                    do {
                        // Convert the data to JSON
                        let jsonSerialized = try JSONSerialization.jsonObject(with: data, options: []) as? [String : Any]
                        
                        if let json = jsonSerialized as? [String: Any]{
                            let venue = json["response"]["groups"][0]["items"][0]["venue"]["name"] as? String
                            print(venue)
                        }
                    }  catch let error as NSError {
                        print(error.localizedDescription)
                    }
                } else if let error = error {
                    print(error.localizedDescription)
                }
            }
            task.resume()
        } else {
            print("couldnt open")
        }
 
        */
        // var name : String = ""
        // Asynchronous Http call to your api url, using URLSession:
        URLSession.shared.dataTask(with: URL(string: "https://api.foursquare.com/v2/venues/explore?near=SanJose,CA&v=20200607&limit=3&client_id=UNXKPYYYPY2PQFGNYL3KXWTKGNT20SO4ISO0YDROW0HORX2W&client_secret=QWPXY050I0NWIEIGIGHGNUBM0XXWN42SNS2XGBGKL3RXBKP3&query=coffee")!) { (data, response, error) -> Void in
            // Check if data was received successfully
            if error == nil && data != nil {
                
                do {
                    // Convert to dictionary where keys are of type String, and values are of any type
                    let json = try JSONSerialization.jsonObject(with: data!, options: .mutableContainers) as! [String: Any]
                    
                    guard let jsonP = json["response"] as? [String: Any] else{
                        return
                    }
                    let groups = jsonP["groups"] as! NSArray
                    let smthg = groups[0] as! NSDictionary
                    let items = smthg["items"] as! NSArray
                    
                    let item1 = items[0] as! NSDictionary
                    let venue = item1["venue"] as! NSDictionary
                    let name1 = venue["name"]
                    print(name1)
                    
                    let item2 = items[1] as! NSDictionary
                    let venue2 = item2["venue"] as! NSDictionary
                    let name2 = venue2["name"]
                    print(name2)
                    
                    let item3 = items[2] as! NSDictionary
                    let venue3 = item3["venue"] as! NSDictionary
                    let name3 = venue3["name"]
                    print(name3)
                    
                    // put in labels
                    
                    self.resultsLabel.text = "1. \(name1!)"
                    self.results2Label.text = "2. \(name2!)"
                    self.results3Label.text = "3. \(name3!)"
                } catch {
                    // Something went wrong
                    self.resultsLabel.text = "1. ah"
                    self.results2Label.text = "2. eh"
                    self.results3Label.text = "3. oh"
                }
            }
            }.resume()
        
    }
    
}

