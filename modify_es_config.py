import yaml

CONFIG_FILE = '/etc/elasticsearch/elasticsearch.yml'
CONFIG_SOURCE = 'source-elasticsearch.yml'
CONFIG_TARGET = 'result-elasticsearch.yml'


with open(CONFIG_SOURCE) as f:
     config = yaml.load(f)

#print config

#config["io.fabric8.elasticsearch.authentication.users"].append("system.admin")
#config["searchguard"]["authentication"]["authorization"]["settingsdb"]["roles"]["admin"] = ["admin"]
config["searchguard"]["actionrequestfilter"]["fluentd"]["allowed_actions"] = ["cluster:*", "indices:admin*", "indices:data*"]
config["searchguard"]["allow_all_from_loopback"] = True


#config["openshift"]["acl"]["users"].append("system.admin")
#config["openshift"]["acl"]["system.admin"]["bypass"] = ["*"]
#config["openshift"]["acl"]["system.admin.*.comment"] = "Admin user can do anything"

with open(CONFIG_TARGET, "w") as f:
    yaml.dump(config, f)
